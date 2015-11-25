# coding: utf-8
import os
import subprocess
import json
import urllib2
import time
import re
from datetime import datetime

from wbc.region.models import Quarter
from wbc.projects.models import Project


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

        # get time since last download
        try:
            time_delta = time.time() - os.stat('/tmp/imverfahren.json').st_ctime
        except OSError:
            time_delta = 86400

        # download data if older than 10 minutes
        if time_delta > 600:
            try:
                os.remove('/tmp/imverfahren.json')
            except OSError:
                pass

            # call org2org to fetch the bplan geojson from the FIZ-Broker
            print "querying geodienste-hamburg.de WFS server"
            cmd = 'ogr2ogr -overwrite -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON /tmp/imverfahren.json WFS:"http://geodienste-hamburg.de/HH_WFS_Bebauungsplaene" app:imverfahren'
            subprocess.call(cmd,shell=True);

        # open geojson
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
            try:
                if feature['properties']['feststellung'].lower() == 'ja':
                    project_values['active'] = False
                else:
                    project_values['active'] = True
            except KeyError:
                project_values['active'] = True

            # update the place or create a new one
            project, created = Project.objects.update_or_create(identifier=project_values['identifier'], defaults=project_values)
            if created:
                importEvent = {
                    'description': "Bauprojekt aus dem  Planportal importiert.",
                    'link': "http://www.hamburg.de/planportal/",
                    'begin': datetime.now()
                }

                link = feature['properties'].get('hotlink_iv', '')
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
