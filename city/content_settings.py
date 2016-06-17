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
    'blog'    : True,
    'lexikon' : True,
    'account' : True,
}

#TOP BOXES ON STARTPAGE
STARTPAGE_OVERVIEW_ICONS = [
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde 3000+ Baupläne', 'link' : reverse_lazy('search') },
    {'text' : 'Im Lexikon stöbern.', 'icon': 'fa-book', 'overlay': 'Erfahre mehr über Bebauungspläne, Gesetze und Verfahren.', 'link' : reverse_lazy('process') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Aktuelle Bauprojekte', 'icon': 'fa-lightbulb-o', 'overlay': 'Aktuell im Verfahren befindliche Bebauungspläne', 'link' : reverse_lazy('search') },
    {'text' : 'Historische Bebauungspläne', 'icon': 'fa-university', 'overlay': 'Stöber durch die Hamburgische Baugeschichte seit 1949.', 'link' : reverse_lazy('search') },
    {'text' : 'Stadtteile', 'icon': 'fa-building-o', 'overlay': 'In Arbeit...', 'link' : reverse_lazy('search') },
]


#SEARCH
DEFAULT_VIEW_MAP   = True     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern

