from os.path import join, normpath
from os import environ
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS += [".atlgameday.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gameday',
        'USER': 'gameday',
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600,
        'KEY_PREFIX': 'gameday',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ.get('MAIL_HOST')
EMAIL_PORT = environ.get('MAIL_PORT')
EMAIL_HOST_USER = environ.get('MAIL_USER')
EMAIL_HOST_PASSWORD = environ.get('MAIL_PASS')
EMAIL_USE_TLS = True
