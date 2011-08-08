from django.conf.urls.defaults import *

urlpatterns = patterns('puzzles.views',
    (r'^$', 'index'),
    (r'^(?P<page>[\w-]+)$', 'page'),
)



    
