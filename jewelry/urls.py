from django.conf.urls.defaults import *

urlpatterns = patterns('jewelry.views',
    (r'^$', 'index'),
    (r'^pendants/$', 'pendants'),
    (r'^earrings/$', 'earrings'),
    (r'^pins/$', 'pins'),
    (r'^other/$', 'other'),
    (r'^build/$', 'build'),
#    (r'^(?P<page>[^\.^/]+.html)$', 'page'),
#    (r'^(?P<key>[^\.^/]+)$', 'detail'),
    (r'^(?P<key>[\w-]+)$', 'detail'),
)
