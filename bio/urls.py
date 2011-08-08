# bio/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('bio.views',
    (r'^$', 'index'),
    (r'^contact$', 'contact'),
    (r'^subscribe$', 'subscribe'),
    (r'^contact/$', 'contact'),
    (r'^(?P<page>[\w-]+)$', 'page'),
#    (r'^(?P<page>.*.html)$', 'page'),
)

    
