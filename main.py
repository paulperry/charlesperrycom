#!/usr/bin/env python
#
# charlesperry.com 

import os,sys,logging

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#http://stackoverflow.com/questions/2568257/google-app-engine-python-importerror-no-module-named-django
# if not os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/non_gae_indicator'):
    # GAE
from google.appengine.dist import use_library
use_library('django', '1.2')

# check this for debug support
# http://code.google.com/p/googleappengine/issues/detail?id=308

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

# Log errors.

#django.dispatch.dispatcher.connect(
#   log_exception, django.core.signals.got_request_exception)
#django.dispatch.dispatcher.Signal.connect(
#  django.core.signals.got_request_exception, log_exception)

# Unregister the rollback event handler.
#django.dispatch.dispatcher.disconnect(
#    django.db._rollback_on_exception,
#    django.core.signals.got_request_exception)

django.dispatch.dispatcher.Signal.disconnect(
  django.core.signals.got_request_exception,
  django.db._rollback_on_exception)

def main():
  # Ensure the Django zipfile is in the path if required.
#  if have_django_zip and django_zip_path not in sys.path:
#    sys.path.insert(1, django_zip_path)

  # Set the logging level in the main function
  logging.getLogger().setLevel(logging.DEBUG)  
  
  # Create a Django application for WSGI.
  application = django.core.handlers.wsgi.WSGIHandler()

  # Run the WSGI CGI handler with that application.
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
