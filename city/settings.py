# -*- coding: utf-8 -*-
import os
from local import *

INSTALLED_APPS = (
    # django
    'django_admin_bootstrapped',
    # 'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django_extensions',
    # other dependencies
    'rest_framework',
    'rest_framework_gis',
    'widget_tweaks',
    'markdown',
    'compressor',
    # we build city apps
    'wbc.core',
    'wbc.region',
    'wbc.process',
    'wbc.notifications',
    # 'wbc.comments',
    'wbc.stakeholder',
    'wbc.tags',
    'wbc.projects',
    'wbc.events',
    'wbc.blog',
    'wbc.accounts',
    'wbc.encyclopedia',
    #'wbc.buildings'
    # 'rolodex',
    'sortedm2m',
    'photologue',
    # 'sorl.thumbnail',
    'taggit',
    'taggit_templatetags',
    # 'taggit_labels',
    'haystack',
    'django_markdown',
    'tinymce',
    'registration',
    'simple_history',
    'guardian',
    'threadedcomments',
    'django_comments',
    'crispy_forms',
    'rosetta',
    'django_makemessages_xgettext',    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT,'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wbc.core.context_processors.settings',
            ],
        },
    },
]

ROOT_URLCONF = 'city.urls'
WSGI_APPLICATION = 'city.wsgi.application'
SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

LANGUAGE_CODE = 'de-DE'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    "locale",
)

from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT,'media_root/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static_root/')

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = False

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

FEED_TITLE = "Polis - by www.We-Build.City (Veröffentlichungen)"
FEED_DESCRIPTION = "Veröffentlichungen zu Bauvorhaben in Polis - by www.We-Build.City"


TILES_URL = 'http://{s}.tiles.we-build.city/hamburg/{z}/{x}/{y}.jpg'

TILES_OPT = {
    'attribution': 'Map data &copy; 2012 OpenStreetMap contributors',
    'maxZoom': 17,
    'minZoom': 10,
    'zIndex': 0,
    'reuseTiles': 1
}

DEFAULT_VIEW = {
    'lat': 53.550556,
    'lon': 10.0,
    'zoom': 11
}


MARKDOWN_EDITOR_SKIN = 'simple'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_HTML = False
INFO_EMAIL = "info@we-build.city"


TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")

TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tiny_mce/")
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'relative_urls' : False
}

# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True

#GUARDIAN
ANONYMOUS_USER_ID = None


HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

COMMENTS_APP = 'threadedcomments'
# FLUENT_COMMENTS_EXCLUDE_FIELDS = ('url')
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#Translation Rosetta
#ROSETTA_WSGI_AUTO_RELOAD
#ROSETTA_UWSGI_AUTO_RELOAD

