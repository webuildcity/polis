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
    {'text' : 'Suche nach Ideen & Projekten', 'icon': 'fa-map-o', 'overlay': 'Finde hier mehr als 70 Ideen & Projekte', 'link' : reverse_lazy('search') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Mobilität', 'icon': 'fa-car', 'overlay': 'Mobilitätsthemen im Landkreis', 'link' : reverse_lazy('search'), 'params' : 'tags=Mobilität' },
    {'text' : 'Familienfreundlichkeit', 'icon': 'fa-heart', 'overlay': 'Alles zum Thema Familienfreundlichkeit', 'link' : reverse_lazy('search'), 'params' : 'tags=Familienfreundlichkeit'  },
    {'text' : 'Arbeitsmarkt', 'icon': 'fa-clock-o', 'overlay': 'Ideen zum Arbeitsmarkt', 'link' : reverse_lazy('search'), 'params' : 'tags=Arbeitsmarkt'  },
    {'text' : 'Bildung', 'icon': 'fa-graduation-cap', 'overlay': 'Bildungsideen', 'link' : reverse_lazy('search'), 'params' : 'tags=Bildung'  },
    {'text' : 'Infrastruktur', 'icon': 'fa-train', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Infrastruktur'  },
    {'text' : 'Kultur und Freizeit', 'icon': 'fa-coffee', 'overlay': 'Kulturprojekte und Ideen', 'link' : reverse_lazy('search'), 'params' : 'tags=Kultur'  },
    {'text' : 'Umwelt', 'icon': 'fa-pagelines', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Umwelt'  },
    {'text' : 'Benachteiligungen abbauen', 'icon': 'fa-ban', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Benachteiligungen'  },
    {'text' : 'Regionale Produkte', 'icon': 'fa-compass', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Regionales'  },
    {'text' : 'Tourismus', 'icon': 'fa-mao-o', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Tourismus'  },
    {'text' : 'Gutes Miteinander', 'icon': 'fa-thumbs-o-up', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Miteinander'  },
    {'text' : 'Weitere Ideen', 'icon': 'fa-plus', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Weiteres'  },

]


#SEARCH
DEFAULT_VIEW_MAP   = False     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern
SHOW_ADDITIONAL_FILTER = False    # switchtes additional filters on/off
TERMINATED_PROJECTS = False
