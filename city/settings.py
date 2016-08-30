# -*- coding: utf-8 -*-
import os
from local import *
from content_settings import * 

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
    'wbc.images',
    #'wbc.buildings'
    # 'rolodex',
    'sortedm2m',
    # 'sorl.thumbnail',
    'taggit',
    'taggit_templatetags',
    # 'taggit_labels',
    'haystack',
    'django_markdown',
    'tinymce',
    'simple_history',
    'guardian',
    'threadedcomments',
    'django_comments',
    'crispy_forms',
    'imagekit',
    'registration',
    'rosetta',
    'django_makemessages_xgettext',
    'star_ratings',
    'etherpad_lite',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'wbc.core.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'wbc.core.backends.DualModelBackend', # this is default
    # 'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT,'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.csrf',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wbc.core.context_processors.settings',
                'django.core.context_processors.i18n',
                'social.apps.django_app.context_processors.backends',
                # 'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

ROOT_URLCONF = 'city.urls'
WSGI_APPLICATION = 'city.wsgi.application'
SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# PROJECT PATH TO LOAD ALL LOCALE FOLDERS CORRECTLY
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCALE_PATHS = (
    "locale",
    os.path.join(PROJECT_PATH, '../locale'),
)

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'amelinghausen'
LANGUAGES = [
    ('de',  _('German')),
    ('en',  _('English')),
    ('pt',  _('Brazilian')),
    ('jdd', _('JugendDemografieDialog')),
    ('amelinghausen', _('Amelinghausen')),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT,'media_root/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static_root/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

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


# TILES_URL = 'https://{s}.tiles.we-build.city/lichtenfels/{z}/{x}/{y}.png'
TILES_URL = 'https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHVuZGVsaXVzIiwiYSI6ImNpa29kc2RsZDAwYWN2c200OWc4ZmNuZWMifQ.EXdvNd6AcfSVZ0Yg07SOwA'

TILES_OPT = {
    'attribution': 'Map data &copy; 2016 OpenStreetMap contributors',
    'maxZoom': 17,
    'minZoom': 10,
    'zIndex': 0,
    'reuseTiles': 1
}

DEFAULT_VIEW = {
    'lat': 53.0925144,
    'lon': 10.2089544,
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

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social.pipeline.user.create_user',

    # Create the record that associated the social account with this user.
    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social.pipeline.user.user_details',
    'city.pipeline.save_profile_picture',
)