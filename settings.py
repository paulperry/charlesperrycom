# Django settings for charlesperry site project.
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = ['charlesperry.com', 'www.charlesperry.com', 'localhost', '127.0.0.1']

ADMINS = (
    # ('Your Name', 'pop@paulperry.net'),
)

MANAGERS = ADMINS

# Database configuration disabled - using file-based data storage
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# support changing the host name for the app
# port = os.environ['SERVER_PORT']
# if port and port != '80':
#     HOST_NAME = '%s:%s' % (os.environ['SERVER_NAME'], port)
# else:
#     HOST_NAME = os.environ['SERVER_NAME']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '#a1g)i%hz+f)44a0wea9ln!g+#=#tke!0@-k)gt=&m#ec-1235')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    
    'sculpture',
    'bio',
    'puzzles',
    'jewelry',
    'chairs',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

WSGI_APPLICATION = 'main.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() in ('true', '1', 'yes')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@charlesperry.com')

# For development, you can use console backend to print emails to console
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




