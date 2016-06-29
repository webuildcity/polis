# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse

#GENERAL SETTINGS
DETAILS_TABS = {
    'info' : False,
    '3d' : False,
    'images' : True,
    'events' : True,
    'stakeholder' : True,
    'discussion' : True,
    'map' : False,
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
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde mehr als 70 Ideen Projekte', 'link' : reverse_lazy('search') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Mobilität', 'icon': 'fa-car', 'overlay': 'Mobilitätsthemen im Landkreis', 'link' : reverse_lazy('search'), 'params' : 'tags=Mobilität' },
    {'text' : 'Familienfreundlichkeit', 'icon': 'fa-heart', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Arbeitsmarkt', 'icon': 'fa-clock-o', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Bildung', 'icon': 'fa-graduation-cap', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Infrastruktur', 'icon': 'fa-train', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Kultur und Freizeit', 'icon': 'fa-coffee', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Umwelt', 'icon': 'fa-pagelines', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Benachteiligungen abbauen', 'icon': 'fa-ban', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Regionale Produkte', 'icon': 'fa-compass', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Tourismus', 'icon': 'fa-mao-o', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Gutes Miteinander', 'icon': 'fa-thumbs-o-up', 'overlay': '', 'link' : reverse_lazy('search') },
    {'text' : 'Weitere Ideen', 'icon': 'fa-plus', 'overlay': '', 'link' : reverse_lazy('search') },

]


#SEARCH
DEFAULT_VIEW_MAP   = False     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern

