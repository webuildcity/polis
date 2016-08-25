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

#DOOOOOOOOOOOOOOO THIS
GENERAL_CONTENT = {
    'blog'    : False,
    'lexikon' : False,
    'account' : True,
}

#TOP BOXES ON STARTPAGE
STARTPAGE_OVERVIEW_ICONS = [
    {'text' : 'Neue Ideen & Orte', 'icon': 'fa-lightbulb-o', 'overlay': 'Neue Orte aus den Workshops', 'link' : reverse_lazy('search') },
    
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') }
]


#SEARCH
DEFAULT_VIEW_MAP   = True     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern
SHOW_ADDITIONAL_FILTER = True    # switchtes additional filters on/off
TERMINATED_PROJECTS = True
