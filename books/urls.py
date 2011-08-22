# books/urls.py
from django.conf.urls.defaults import *

#urlpatterns = patterns('django.views.generic.simple',
#    (r'^$', 'direct_to_template', {'template': 'books/index.html'}),
#    (r'(.+)\.html$', 'direct_to_template'),
#)

urlpatterns = patterns('books.views',
    (r'^$', 'index'),
    (r'^(?P<page>[\w-]+)$', 'page'),
)



    
