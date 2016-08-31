# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse

#GENERAL SETTINGS
DETAILS_TABS = {
    'info' : True,
    '3d' : False,
    'images' : True,
    'events' : False,
    'stakeholder' : True,
    'discussion' : True,
    'map' : True,
    'etherpad' : True,
}

ORDER_BTNS = [
    {'value' : 'name', 'text' : 'Ideen'},
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
    {'text' : 'Gesamtübersicht über alle Ideen & Projekte', 'icon': 'fa-lightbulb-o', 'overlay': 'Klicke hier für die Übersicht', 'link' : reverse_lazy('search') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Gruppe 1', 'icon': 'fa-users', 'overlay': 'Gruppe 1', 'link' : reverse_lazy('search'), 'params' : 'tags=Gruppe1' },
    {'text' : 'Gruppe 2', 'icon': 'fa-users', 'overlay': 'Gruppe 2', 'link' : reverse_lazy('search'), 'params' : 'tags=Gruppe2' },
    {'text' : 'Gruppe 3', 'icon': 'fa-users', 'overlay': 'Gruppe 3', 'link' : reverse_lazy('search'), 'params' : 'tags=Gruppe3' },
]

#SEARCH
DEFAULT_VIEW_MAP   = False     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern
SHOW_ADDITIONAL_FILTER = False    # switchtes additional filters on/off
TERMINATED_PROJECTS = False
