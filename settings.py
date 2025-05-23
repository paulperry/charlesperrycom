# Django settings for charlesperry site project.
import os

# http://stackoverflow.com/questions/2568257/google-app-engine-python-importerror-no-module-named-django
if not os.path.exists(os.getcwd() + '/non_gae_indicator'): # GAE
    DEBUG = False
    PREPEND_WWW = True
else:  # localhost
    DEBUG = True
    PREPEND_WWW = False
PREPEND_WWW = False

#TEMPLATE_DEBUG = DEBUG

import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

ADMINS = (
    # ('Your Name', 'pop@paulperry.net'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''    # 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''      # Or path to database file if using sqlite3.
DATABASE_USER = ''      # Not used with sqlite3.
DATABASE_PASSWORD = ''  # Not used with sqlite3.
DATABASE_HOST = ''      # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''      # Set to empty string for default. Not used with sqlite3.

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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/Users/paulperry/Documents/sites/charlesperrycom/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://www.charlesperry.com/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#a1g)i%hz+f)44a0wea9ln!g+#=#tke!0@-k)gt=&m#ec-1235'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
        ('django.template.loaders.cached.Loader',(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
#            'forum.modules.template_loader.module_templates_loader',
#            'forum.skins.load_template_source',
            )),
    ]
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
##     'django.template.loaders.eggs.load_template_source',
#)

MIDDLEWARE_CLASSES = (
# http://code.google.com/appengine/docs/python/tools/appstats.html
#    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'minidetector.Middleware',
#    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

INSTALLED_APPS = (
#    'appengine_django',
    'sculpture',
    'bio',
    'puzzles',
    'jewelry',
    'chairs',
#    'django.contrib.redirects',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
)




