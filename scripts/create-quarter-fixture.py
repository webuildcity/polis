#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

districts = {
    "Hamburg-Mitte": 2,
    "Altona": 3,
    "Eimsbüttel": 4,
    "Hamburg-Nord": 5,
    "Wandsbek": 6,
    "Bergedorf": 7,
    "Harburg": 8
}

quarters = {
    "Hamburg-Altstadt": "Hamburg-Mitte",
    "HafenCity": "Hamburg-Mitte",
    "Neustadt": "Hamburg-Mitte",
    "St.Pauli": "Hamburg-Mitte",
    "St.Georg": "Hamburg-Mitte",
    "Hammerbrook": "Hamburg-Mitte",
    "Borgfelde": "Hamburg-Mitte",
    "Hamm": "Hamburg-Mitte",
    "Horn": "Hamburg-Mitte",
    "Billstedt": "Hamburg-Mitte",
    "Billbrook": "Hamburg-Mitte",
    "Rothenburgsort": "Hamburg-Mitte",
    "Veddel": "Hamburg-Mitte",
    "Wilhelmsburg": "Hamburg-Mitte",
    "Kleiner Grasbrook": "Hamburg-Mitte",
    "Steinwerder": "Hamburg-Mitte",
    "Waltershof": "Hamburg-Mitte",
    "Finkenwerder": "Hamburg-Mitte",
    "Neuwerk": "Hamburg-Mitte",
    "Altona-Altstadt": "Altona",
    "Sternschanze": "Altona",
    "Altona-Nord": "Altona",
    "Ottensen": "Altona",
    "Bahrenfeld": "Altona",
    "Groß Flottbek": "Altona",
    "Othmarschen": "Altona",
    "Lurup": "Altona",
    "Osdorf": "Altona",
    "Nienstedten": "Altona",
    "Blankenese": "Altona",
    "Iserbrook": "Altona",
    "Suelldorf": "Altona",
    "Rissen": "Altona",
    "Eimsbuttel": "Eimsbüttel",
    "Rotherbaum": "Eimsbüttel",
    "Harvestehude": "Eimsbüttel",
    "Hoheluft-West": "Eimsbüttel",
    "Lokstedt": "Eimsbüttel",
    "Niendorf": "Eimsbüttel",
    "Schnelsen": "Eimsbüttel",
    "Eidelstedt": "Eimsbüttel",
    "Stellingen": "Eimsbüttel",
    "Hoheluft-Ost": "Hamburg-Nord",
    "Eppendorf": "Hamburg-Nord",
    "Gross-Borstel": "Hamburg-Nord",
    "Alsterdorf": "Hamburg-Nord",
    "Winterhude": "Hamburg-Nord",
    "Uhlenhorst": "Hamburg-Nord",
    "Hohenfelde": "Hamburg-Nord",
    "Barmbek-Sued": "Hamburg-Nord",
    "Dulsberg": "Hamburg-Nord",
    "Barmbek-Nord": "Hamburg-Nord",
    "Ohlsdorf": "Hamburg-Nord",
    "Fuhlsbuettel": "Hamburg-Nord",
    "Langenhorn": "Hamburg-Nord",
    "Eilbek": "Wandsbek",
    "Wandsbek": "Wandsbek",
    "Marienthal": "Wandsbek",
    "Jenfeld": "Wandsbek",
    "Tonndorf": "Wandsbek",
    "Farmsen-Berne": "Wandsbek",
    "Bramfeld": "Wandsbek",
    "Steilshoop": "Wandsbek",
    "Wellingsbuettel": "Wandsbek",
    "Sasel": "Wandsbek",
    "Poppenbuettel": "Wandsbek",
    "Hummelsbuttel": "Wandsbek",
    "Lemsahl-Mellingstedt": "Wandsbek",
    "Duvenstedt": "Wandsbek",
    "Wohldorf-Ohlstedt": "Wandsbek",
    "Bergstedt": "Wandsbek",
    "Volksdorf": "Wandsbek",
    "Rahlstedt": "Wandsbek",
    "Lohbruegge": "Bergedorf",
    "Bergedorf": "Bergedorf",
    "Curslack": "Bergedorf",
    "Altengamme": "Bergedorf",
    "Neuengamme": "Bergedorf",
    "Kirchwerder": "Bergedorf",
    "Ochsenwerder": "Bergedorf",
    "Reitbrook": "Bergedorf",
    "Allermohe": "Bergedorf",
    "Billwerder": "Bergedorf",
    "Moorfleet": "Bergedorf",
    "Tatenberg": "Bergedorf",
    "Spadenland": "Bergedorf",
    "Neuallermohe": "Bergedorf",
    "Harburg": "Harburg",
    "Neuland": "Harburg",
    "Gut Moor": "Harburg",
    "Wilstorf": "Harburg",
    "Ronneburg": "Harburg",
    "Langenbek": "Harburg",
    "Sinstorf": "Harburg",
    "Marmstorf": "Harburg",
    "Eissendorf": "Harburg",
    "Heimfeld": "Harburg",
    "Moorburg": "Harburg",
    "Altenwerder": "Harburg",
    "Hausbruch": "Harburg",
    "Neugraben-Fischbek": "Harburg",
    "Francop": "Harburg",
    "Neuenfelde": "Harburg",
    "Cranz": "Harburg",
}


data = []

for i,key in enumerate(sorted(quarters)):
    data.append({
        "fields": {
            "created": "2015-01-11T20:00:00Z",
            "name": key,
            "updated": "2013-06-11T20:00:00Z"
        },
        "model": "region.entity",
        "pk": i + 8
    })

for i,key in enumerate(sorted(quarters)):
    data.append({
        "fields": {
            "district": districts[quarters[key]],
        },
        "model": "region.quarter",
        "pk": i + 8
    })

print json.dumps(data)