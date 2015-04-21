# coding=utf8
import os,sys
sys.path.append('/path/to/wbc/lib')

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'this is a not very secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wbh',
        'USER': 'wbh'
    }
}

SITE_TITLE = 'Wir bauen Hamburg'
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
SITE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'info@wir-bauen-hamburg.de'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True

# FACEBOOK_APIKEY = 'XXXXXXXXXXXXXXX'
