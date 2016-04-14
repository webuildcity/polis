
# coding=utf8
import os,sys
#sys.path.append('/path/to/wbc/lib')

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'this is a not very secret key'

# SESSION_COOKIE_SECURE = False

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    # }

    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': '../database.sqlite3' # path to database file
     }
}

HAYSTACK_CONNECTIONS = {
         'default': {
         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
         'URL': 'http://127.0.0.1:9200/',
         'INDEX_NAME': 'haystackindex',
     },
}

SITE_TITLE = 'Polis - by We-Build.City'
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
SITE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_FROM = ''

#EMAIL_HOST = ''
#EMAIL_PORT = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True

# FACEBOOK_APIKEY = 'XXXXXXXXXXXXXXX'
