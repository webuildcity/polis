# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy

#GENERAL SETTINGS
DETAILS_TABS = {
    'info' : True,
    '3d' : True,
    'images' : True,
    'events' : True,
    'stakeholder' : True,
    'discussion' : True,
    'map' : True,
    'etherpad' : True,
}

ORDER_BTNS = [
    {'value' : 'name', 'text' : 'Name'},
    {'value' : '-created', 'text' : 'Datum'},
    # {'value' : '-num_stakeholder', 'text' : '# Beteiligte'},
    {'value' : '-ratings_avg', 'text' : 'Bewertung'},
    # {'value' : '-ratings_count', 'text' : '# Bewertungen'},
]

#SWITCH ON/OFF PARTS OF THE WBC APP
GENERAL_CONTENT = {
    'blog'    : True,
    'lexikon' : True,
    'account' : True,
    'wbcrating': True,
    'starrating': True,
    'featured' : True,
    'updownvote': True,
    'social_media_share': True,
}

#TOP BOXES ON STARTPAGE
STARTPAGE_OVERVIEW_ICONS = [
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') },
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') },
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') }
]


#SEARCH
DEFAULT_VIEW_MAP   = True     # True = map, False = kachel, None = list
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern
SHOW_ADDITIONAL_FILTER = True    # switchtes additional filters on/off
TERMINATED_PROJECTS = True
