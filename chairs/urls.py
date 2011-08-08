from django.conf.urls.defaults import *

#urlpatterns = patterns('django.views.generic.simple',
#    (r'^$', 'direct_to_template', {'template': 'chairs/index.html'}),
#    (r'(.+)\.html$', 'direct_to_template'),
#)

urlpatterns = patterns('chairs.views',
    (r'^$', 'index'),
    (r'^(?P<page>[\w-]+)$', 'page'),
#    (r'^(?P<page>[\w-]+\.html)$', 'page'),
)



    
