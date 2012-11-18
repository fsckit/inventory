# Django settings for inventory project development
import os
from app.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Probably don't add yourself here
ADMINS = ( )
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db/default.db',
    }
}

EMAIL_FROM = 'no-reply@genericon.union.rpi.edu'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = ''
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4ktv5%y20q)-6law0pfuu14ukke9un-5f4c(5waqkac3j5x9wt'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scripts.wsgi.application'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
