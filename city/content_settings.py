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

#SWITCH ON/OFF PARTS OF THE WBC APP
GENERAL_CONTENT = {
    'blog'    : False,
    'lexikon' : False,
    'account' : True,
    'wbcrating': True,
    'starrating': True,
    'featured' : True,
    'updownvote': True,
    'social_media_share': True,
}

#TOP BOXES ON STARTPAGE
STARTPAGE_OVERVIEW_ICONS = [
    {'text' : 'Gesamtübersicht über alle Ideen & Projekte', 'icon': 'fa-lightbulb-o', 'overlay': 'Klicke hier für die Übersicht', 'link' : reverse_lazy('search') },
]

#BOTTOM BOXES ON STARTPAGE
STARTPAGE_TOPIC_ICONS = [
    {'text' : 'Wirtschaft, Arbeits- und Ausbildungsplätze', 'icon': 'fa-line-chart', 'overlay': 'Wirtschaft, Arbeits- und Ausbildungsplätze', 'link' : reverse_lazy('search'), 'params' : 'tags=Wirtschaft'  },
    {'text' : 'Mobilität', 'icon': 'fa-car', 'overlay': 'Mobilität', 'link' : reverse_lazy('search'), 'params' : 'tags=Mobilität' },
    {'text' : 'Bildung', 'icon': 'fa-graduation-cap', 'overlay': 'Bildungsideen', 'link' : reverse_lazy('search'), 'params' : 'tags=Bildung'  },
    {'text' : 'Familie', 'icon': 'fa-heart', 'overlay': 'Alles zum Thema Familie', 'link' : reverse_lazy('search'), 'params' : 'tags=Familie'  },
    {'text' : 'Infrastruktur', 'icon': 'fa-train', 'overlay': '', 'link' : reverse_lazy('search'), 'params' : 'tags=Infrastruktur'  },
    {'text' : 'Kultur und Freizeit', 'icon': 'fa-coffee', 'overlay': 'Kulturprojekte und Ideen', 'link' : reverse_lazy('search'), 'params' : 'tags=Kultur'  },
    {'text' : 'Zivilgesellschaft / Ehrenamt', 'icon': 'fa-university', 'overlay': 'Zivilgesellschaft / Ehrenamt', 'link' : reverse_lazy('search'), 'params' : 'tags=Zivilgesellschaft'  },
    {'text' : 'Wohnen', 'icon': 'fa-home', 'overlay': 'Wohnen', 'link' : reverse_lazy('search'), 'params' : 'tags=Wohnen'  },
    {'text' : 'Gesundheit', 'icon': 'fa-heartbeat', 'overlay': 'Gesundheit', 'link' : reverse_lazy('search'), 'params' : 'tags=Gesundheit'  },
    {'text' : 'Zuwanderung (Migration)', 'icon': 'fa-universal-access', 'overlay': 'Zuwanderung (Migration)', 'link' : reverse_lazy('search'), 'params' : 'tags=Zuwanderung'  },
    {'text' : 'Alter', 'icon': 'fa-blind', 'overlay': 'Alter', 'link' : reverse_lazy('search'), 'params' : 'tags=Alter'  },
    {'text' : 'Demokratie & Partizipation', 'icon': 'fa-hand-paper-o', 'overlay': 'Demokratie & Partizipation', 'link' : reverse_lazy('search'), 'params' : 'tags=Demokratie'  },
    {'text' : 'Öffentliche Verwaltung', 'icon': 'fa-university', 'overlay': 'Öffentliche Verwaltung', 'link' : reverse_lazy('search'), 'params' : 'tags=Verwaltung'  },

]

DEFAULT_VIEW_MAP   = None     # karte oder listenansicht zuerst
SHOW_ENTITY_FILTER = True   # kann man nach entities filtern
SHOW_ADDITIONAL_FILTER = False    # switchtes additional filters on/off
TERMINATED_PROJECTS = False
