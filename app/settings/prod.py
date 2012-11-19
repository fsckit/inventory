# Django settings for inventory project production
import os
import dj_database_url
from app.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Doug', 'douglas.patti@gmail.com'),
    # Add name/email here to be notified of production errors
)
MANAGERS = ADMINS

DATABASES = { 'default': dj_database_url.config() }

# Configuration for SendGrid on Heroku
EMAIL_FROM = 'Genericon <no-reply@genericon.union.rpi.edu>'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True

MEDIA_URL = ''
STATIC_URL = '/static/'

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

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
        },
        'console_print': {
          'level': 'ERROR',
          'filters': ['require_debug_false'],
          'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console_print'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
