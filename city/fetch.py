# coding: utf-8
import sys
import os
import subprocess
import json
import urllib2
import time
import re
import csv
from datetime import datetime
from lxml import html
import lxml
import requests
from django.core.files import File
from django.conf import settings

import wand
from wand.image import Image

from wbc.region.models import Quarter
from wbc.projects.models import Project, BufferArea, ProjectAttachment
from wbc.events.models import Publication
from wbc.process.models import ProcessStep

class ProjectFetcher():

    def fetch(self):

        umlaut_quarters = {
            "Barmbek-Sued": "Barmbek-Süd",
            "Fuhlsbuettel": "Fuhlsbüttel",
            "Lohbruegge": "Lohbrügge",
            "Poppenbuettel": "Poppenbüttel",
            "Suelldorf": "Sülldorf",
            "Wellingsbuettel": "Wellingsbüttel"
        }

        # get time since last downloadc     
        try:
            time_delta = time.time() - os.stat('/tmp/imverfahren.json').st_ctime
            print time_delta
        except OSError:
            time_delta = 86400

        # download data if older than 10 minutes
        if time_delta > 10:
            try:
                os.remove('/tmp/imverfahren.json')
            except OSError:
                pass

            # call org2org to fetch the bplan geojson from the FIZ-Broker
            print "querying geodienste-hamburg.de WFS server"
            cmd = 'ogr2ogr -overwrite -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON /tmp/imverfahren.json WFS:"http://geodienste-hamburg.de/HH_WFS_Bebauungsplaene" app:prosin_imverfahren'
            subprocess.call(cmd,shell=True);

        # open geojson
        print os.path.dirname(os.path.realpath('/tmp/imverfahren.json'))

        geojson = json.load(open('/tmp/imverfahren.json','r'))
        n = 0
        for feature in geojson["features"]:

            # prepare values dictionary
            project_values = {}

            # get identifier
            try:
                project_values['identifier'] = feature['properties']['plan'].replace(' ','').strip()
                cleaned_identifier = project_values['identifier'].replace('Aend','')
                quarters = []
                for quarter in re.findall('([a-zA-Z][a-zA-Z\-\.]+)',cleaned_identifier):
                    if quarter in umlaut_quarters:
                        quarters.append(umlaut_quarters[quarter])
                    else:
                        quarters.append(quarter)
                project_values['name'] = cleaned_identifier
            except KeyError:
                continue

            # switch lat and lon in (multi) polygon and get center
            try:
                latMin,latMax,lonMin,lonMax = 90,-90,180,-180
                if feature['geometry']['type'] == 'Polygon':
                    for path in feature['geometry']['coordinates']:
                        for point in path:
                            # point[0],point[1] = point[1],point[0]
                            latMin = min(latMin,point[0])
                            latMax = max(latMax,point[0])
                            lonMin = min(lonMin,point[1])
                            lonMax = max(lonMax,point[1])
                    project_values['polygon'] = json.dumps([feature['geometry']['coordinates']])
                else:
                    for polygon in feature['geometry']['coordinates']:
                        for path in polygon:
                            for point in path:
                                # point[0],point[1] = point[1],point[0]
                                latMin = min(latMin,point[0])
                                latMax = max(latMax,point[0])
                                lonMin = min(lonMin,point[1])
                                lonMax = max(lonMax,point[1])
                    project_values['polygon'] = json.dumps(feature['geometry']['coordinates'])

                # get lat and lon
                project_values['lat'] = str((latMax + latMin) * 0.5)
                project_values['lon'] = str((lonMax + lonMin) * 0.5)
            except TypeError:
                continue

            project_values['active'] = True
            project_values['isFinished'] = False
            # update the place or create a new one
            project, created = Project.objects.update_or_create(identifier=project_values['identifier'], defaults=project_values)

            # add Tags
            project.tags.add('Bebauungsplan', 'Bebauungsplan im Verfahren', 'B-Plan')

            link = feature['properties'].get('hotlink_iv', '')
            if link:
                #scrape pdfs from project page
                project_page = requests.get(link)
                try:
                    tree = html.fromstring(project_page.content)
                    pdfs = tree.xpath('//a[@class="nscout pdf"]')

                    for pdf in pdfs:
                        pdf_link = 'http://www.hamburg.de'+ pdf.xpath('@href')[0]
                        
                        #check if attachment already exists in database
                        if not ProjectAttachment.objects.filter(source=pdf_link).exists():
                            # title = pdf.xpath('text()')[0].lstrip().split('(')[0][:-1]

                            pdf_name = pdf_link.split('/')[-1]
                            img_name = pdf_name.split('.pdf')[0] + '.png'

                            raw_pdf = urllib2.urlopen(pdf_link)
                            attachment = ProjectAttachment(name=pdf_name, project=project, source=pdf_link)

                            with open('tmp_pdf', 'wb') as f:
                                f.write(raw_pdf.read())

                            with open('tmp_pdf', 'r') as f:
                                pdf_file = File(f, 'r')
                                attachment.attachment.save(pdf_name, pdf_file, True)
                                attachment.save()
                                
                                try:
                                    img= Image(blob=pdf_file)
                                    img = Image(img.sequence[0])
                                    img.format='png' #png to counter background color bug when using jpg
                                    img_url = settings.MEDIA_ROOT + "project_attachments/images/"+ img_name
                                    img.save(filename=img_url)
                                    attachment.image = "project_attachments/images/"+ img_name
                                    attachment.save()
                                except wand.exceptions.DelegateError:
                                    print 'DelegateError', link
                           
                            os.remove('tmp_pdf')
                
                except lxml.etree.XMLSyntaxError:
                    print 'XMLSyntaxError for: ', link

            if created:
                importEvent = {
                    'description': "Bauprojekt aus dem  Planportal importiert.",
                    'link': "http://www.hamburg.de/planportal/",
                    'begin': datetime.now()
                }

                if link:
                    project.link = link.strip()
                    importEvent['link'] = link.strip()

                project.events.create(**importEvent)

                n += 1
                try:
                    for quarter in quarters:
                        q = Quarter.objects.get(name=quarter)
                        project.entities.add(q)
                        project.save()
                except Quarter.DoesNotExist:
                    print 'no quarter for', project_values['identifier']

                # if project.address == '':
                #     # get address from open street map
                #     url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=18&addressdetails=1" % (project.lat, project.lon)

                #     response = urllib2.urlopen(url).read()
                #     data = json.loads(response)
                #     if 'road' in data['address']:
                #         project.address = data['address']['road']
                #     else:
                #         project.address = ''
                #     time.sleep(1.2)

                print project,'(' + ', '.join([str(quarter) for quarter in quarters]) + ')'

        print n,'projects created'

class ProjectFestgestelltFetcher():

    def fetch(self):

        umlaut_quarters = {
            "Barmbek-Sued": "Barmbek-Süd",
            "Fuhlsbuettel": "Fuhlsbüttel",
            "Lohbruegge": "Lohbrügge",
            "Poppenbuettel": "Poppenbüttel",
            "Suelldorf": "Sülldorf",
            "Wellingsbuettel": "Wellingsbüttel"
        }

        # get time since last downloadc     
        try:
            time_delta = time.time() - os.stat('/tmp/festgestellt.json').st_ctime
        except OSError:
            time_delta = 86400

        # download data if older than 10 minutes
        if time_delta > 600:
            try:
                os.remove('/tmp/festgestellt.json')
            except OSError:
                pass

            # call org2org to fetch the bplan geojson from the FIZ-Broker
            print "querying geodienste-hamburg.de WFS server"
            cmd = 'ogr2ogr -overwrite -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON /tmp/festgestellt.json WFS:"http://geodienste-hamburg.de/HH_WFS_Bebauungsplaene" app:hh_hh_planung_festgestellt'
            subprocess.call(cmd,shell=True);

        # open geojson
        print os.path.dirname(os.path.realpath('/tmp/festgestellt.json'))

        geojson = json.load(open('/tmp/festgestellt.json','r'))
        n = 0
        for feature in geojson["features"]:

            # prepare values dictionary
            project_values = {}

            # get identifier
            try:
                project_values['identifier'] = feature['properties']['planrecht'].replace(' ','').strip()
                cleaned_identifier = project_values['identifier'].replace('Aend','')
                quarters = []
                for quarter in re.findall('([a-zA-Z][a-zA-Z\-\.]+)',cleaned_identifier):
                    if quarter in umlaut_quarters:
                        quarters.append(umlaut_quarters[quarter])
                    else:
                        quarters.append(quarter)
                project_values['name'] = cleaned_identifier
            except KeyError:
                continue

            # switch lat and lon in (multi) polygon and get center
            try:
                latMin,latMax,lonMin,lonMax = 90,-90,180,-180
                if feature['geometry']['type'] == 'Polygon':
                    for path in feature['geometry']['coordinates']:
                        for point in path:
                            point[0],point[1] = point[1],point[0]
                            latMin = min(latMin,point[0])
                            latMax = max(latMax,point[0])
                            lonMin = min(lonMin,point[1])
                            lonMax = max(lonMax,point[1])
                    project_values['polygon'] = json.dumps([feature['geometry']['coordinates']])
                else:
                    for polygon in feature['geometry']['coordinates']:
                        for path in polygon:
                            for point in path:
                                point[0],point[1] = point[1],point[0]
                                latMin = min(latMin,point[0])
                                latMax = max(latMax,point[0])
                                lonMin = min(lonMin,point[1])
                                lonMax = max(lonMax,point[1])
                    project_values['polygon'] = json.dumps(feature['geometry']['coordinates'])

                # get lat and lon
                project_values['lat'] = str((latMax + latMin) * 0.5)
                project_values['lon'] = str((lonMax + lonMin) * 0.5)
            except TypeError:
                continue

            # see if is marked active
            # try:
            #     if feature['properties']['feststellung'].lower() == 'ja':
            #         project_values['active'] = False
            #     else:
            #         project_values['active'] = True
            # except KeyError:
            #     project_values['active'] = True
            project_values['active'] = True

            date = feature['properties'].get('feststellung', '')
            if date:
                project_values['finished'] = datetime.strptime(date, '%d.%m.%Y');
            # update the place or create a new one
            project, created = Project.objects.update_or_create(identifier=project_values['identifier'], defaults=project_values)

            link = feature['properties'].get('hotlink', '')
            
            project.tags.add('Bebauungsplan', 'Bebauungsplan festgestellt', 'B-Plan')

            if link:
                pdf_link = link
                
                #check if attachment already exists in database
                if not ProjectAttachment.objects.filter(source=pdf_link).exists():
                    # title = pdf_link.xpath('text()')[0].lstrip().split('(')[0][:-1]
                    try:
                        pdf_name = pdf_link.split('/')[-1]
                        img_name = pdf_name.split('.pdf')[0] + '.png'
                        print pdf_link
                        raw_pdf = urllib2.urlopen(pdf_link)
                        attachment = ProjectAttachment(name=pdf_name, project=project, source=pdf_link)

                        with open('tmp_pdf', 'wb') as f:
                            f.write(raw_pdf.read())

                        with open('tmp_pdf', 'r') as f:
                            pdf_file = File(f, 'r')
                            attachment.attachment.save(pdf_name, pdf_file, True)
                            attachment.save()
                            
                            try:
                                img= Image(blob=pdf_file)
                                img = Image(img.sequence[0])
                                img.format='png' #png to counter background color bug when using jpg
                                img_url = settings.MEDIA_ROOT + "project_attachments/images/"+ img_name
                                img.save(filename=img_url)
                                attachment.image = "project_attachments/images/"+ img_name
                                attachment.save()
                            except wand.exceptions.DelegateError:
                                print 'DelegateError', pdf_link
                        os.remove('tmp_pdf')
                    except urllib2.HTTPError:
                        print 'HTTP Error ', pdf_link

            if date:

                # finishEvent = {
                #     'description': "Bebauungsplan festgestellt.",
                #     'link': link.strip(),
                #     'begin': datetime.strptime(date, '%d.%m.%Y')
                # }
                if len(project.publication_set.all().filter(process_step__name='Feststellung'))==0:
                    pub = Publication(project=project, process_step=ProcessStep.objects.get(name="Feststellung"), begin=datetime.strptime(date, '%d.%m.%Y'))
                    # project.events.add(pub)
                    pub.save()
                    print pub

            if created:
                importEvent = {
                    'description': "Bauprojekt aus dem  Planportal importiert.",
                    'link': "http://www.hamburg.de/planportal/",
                    'begin': datetime.now()
                }
                    

                
                if link:
                    project.link = link.strip()
                    importEvent['link'] = link.strip()
                
                

                project.events.create(**importEvent)

                n += 1
                try:
                    for quarter in quarters:
                        q = Quarter.objects.get(name=quarter)
                        project.entities.add(q)
                        project.save()
                except Quarter.DoesNotExist:
                    print 'no quarter for', project_values['identifier']

                if project.address == '':
                    # get address from open street map
                    url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=18&addressdetails=1" % (project.lat, project.lon)

                    response = urllib2.urlopen(url).read()
                    data = json.loads(response)
                    if 'road' in data['address']:
                        project.address = data['address']['road']
                    else:
                        project.address = ''
                    time.sleep(1.2)

                print project,'(' + ', '.join([str(quarter) for quarter in quarters]) + ')'

        print n,'projects created'


class AusgleichsflaechenFetcher():

    def fetch(self):
        umlaut_quarters = {
            "Barmbek-Sued": "Barmbek-Süd",
            "Fuhlsbuettel": "Fuhlsbüttel",
            "Lohbruegge": "Lohbrügge",
            "Poppenbuettel": "Poppenbüttel",
            "Suelldorf": "Sülldorf",
            "Wellingsbuettel": "Wellingsbüttel"
        }

        # get time since last downloadc     
        try:
            time_delta = time.time() - os.stat('/tmp/ausgleichsflaechen.json').st_ctime
        except OSError:
            time_delta = 86400

        # download data if older than 10 minutes
        if time_delta > 600:
            try:
                os.remove('/tmp/ausgleichsflaechen.json')
            except OSError:
                pass

            # call org2org to fetch the bplan geojson from the FIZ-Broker
            print "querying geodienste-hamburg.de WFS server"
            cmd = 'ogr2ogr -overwrite -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON /tmp/ausgleichsflaechen.json WFS:"http://geodienste-hamburg.de/HH_WFS_Ausgleichsflaechen" Ausgleichsflaechen:Ausgleichsflaechen'
            subprocess.call(cmd,shell=True);

        # open geojson
        geojson = json.load(open('/tmp/ausgleichsflaechen.json','r'))
        n = 0
        for feature in geojson["features"]:

            # prepare values dictionary
            ausgleichsflaechen_values = {}

            # get identifier
            try:
                split_ident = feature['properties']['VORHABEN'].split(' - ', 1)
                ausgleichsflaechen_values['identifier'] = split_ident[0]
                ausgleichsflaechen_values['name'] = split_ident[1]

                quarters = []
                for quarter in re.findall('([a-zA-Z][a-zA-Z\-\.]+)',split_ident[1]):
                    if quarter in umlaut_quarters:
                        quarters.append(umlaut_quarters[quarter])
                    else:
                        quarters.append(quarter)
            except KeyError:
                continue

            # switch lat and lon in (multi) polygon and get center
            try:
                latMin,latMax,lonMin,lonMax = 90,-90,180,-180
                if feature['geometry']['type'] == 'Polygon':
                    for path in feature['geometry']['coordinates']:
                        for point in path:
                            point[0],point[1] = point[1],point[0]
                            latMin = min(latMin,point[0])
                            latMax = max(latMax,point[0])
                            lonMin = min(lonMin,point[1])
                            lonMax = max(lonMax,point[1])
                    ausgleichsflaechen_values['polygon'] = json.dumps([feature['geometry']['coordinates']])
                else:
                    for polygon in feature['geometry']['coordinates']:
                        for path in polygon:
                            for point in path:
                                point[0],point[1] = point[1],point[0]
                                latMin = min(latMin,point[0])
                                latMax = max(latMax,point[0])
                                lonMin = min(lonMin,point[1])
                                lonMax = max(lonMax,point[1])
                    ausgleichsflaechen_values['polygon'] = json.dumps(feature['geometry']['coordinates'])

                # get lat and lon
                ausgleichsflaechen_values['lat'] = str((latMax + latMin) * 0.5)
                ausgleichsflaechen_values['lon'] = str((lonMax + lonMin) * 0.5)
            except TypeError:
                continue

            ausgleichsflaechen_values['area'] =  feature['properties']['FLAECHE']
            ausgleichsflaechen_values['arrangment'] =  feature['properties']['KOMPENSATIONSMASSNAHME']
            ausgleichsflaechen_values['gml_id'] =  feature['properties']['gml_id']


            # see if is marked active
            # try:
            #     if feature['properties']['feststellung'].lower() == 'ja':
            #         project_values['active'] = False
            #     else:
            #         project_values['active'] = True
            # except KeyError:
            #     project_values['active'] = True
            ausgleichsflaechen_values['active'] = True
            # # update the place or create a new one
            buffer_area, created = BufferArea.objects.update_or_create(gml_id=ausgleichsflaechen_values['gml_id'], defaults=ausgleichsflaechen_values)
            # if created:
            #     importEvent = {
            #         'description': "Bauprojekt aus dem  Planportal importiert.",
            #         'link': "http://www.hamburg.de/planportal/",
            #         'begin': datetime.now()
            #     }

            #     link = feature['properties'].get('hotlink_iv', '')
            #     if link:
            #         project.link = link.strip()
            #         importEvent['link'] = link.strip()

            #     project.events.create(**importEvent)
            if created: 
                n += 1
                
            try:
                for quarter in quarters:
                    q = Quarter.objects.get(name=quarter)
                    buffer_area.entities.add(q)
                    buffer_area.save()
            except Quarter.DoesNotExist:
                print 'no quarter for', ausgleichsflaechen_values['identifier']

            #     print project,'(' + ', '.join([str(quarter) for quarter in quarters]) + ')'

        print n,'ausgleichsflaechen created'


class ProjectAfLink():
    def fetch(self):
        n = 0
        with open('data/vorhabennr.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    project = Project.objects.get(name=row['VORHABEN'])
                except Project.DoesNotExist:
                    print row['VORHABEN']
                try:
                    areas = BufferArea.objects.filter(identifier=row['VORHABEN_NR'])
                except BufferArea.DoesNotExist:
                    print row['VORHABEN_NR']

                if project and areas:
                    for area in areas:
                        n += 1
                        area.project = project
                        area.save()

                # print row['VORHABEN_NR']
                # print row['VORHABEN']

        print n,'buffer areas linked with projects'


