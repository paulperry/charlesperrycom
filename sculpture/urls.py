# sculpture urls.py
#
from django.conf.urls.defaults import *

urlpatterns = patterns('sculpture.views',
    (r'^$', 'index_style'),
    (r'^create/$', 'create'),
    (r'^build/$', 'build'),
    (r'^bind/$', 'bind'),
    (r'^all/$', 'all'),
    (r'^tour/$', 'tour'),
    (r'^perry\.kml$', 'genkml'),
    (r'^list/$', 'list'),
    (r'^style/$', 'style'),
    (r'^map/$', 'page', {'page': 'map'}),
    (r'^style/(?P<art_style>planar)/$', 'art_style'),
    (r'^style/(?P<art_style>topological)/$', 'art_style'),
    (r'^style/(?P<art_style>ribbed)/$', 'art_style'),
    (r'^style/(?P<art_style>solid)/$', 'art_style'),
    (r'^material/$', 'material'),
    (r'^material/(?P<art_material>aluminum)/$', 'aluminum'),
    (r'^material/(?P<art_material>bronze)/$', 'bronze'),
    (r'^material/(?P<art_material>other)/$', 'other'),
    (r'^material/(?P<art_material>steel)/$', 'steel'),
    (r'^material/(?P<art_material>stainlesssteel)/$', 'stainlesssteel'),
    (r'^(?P<page>slideshow$)$', 'page'),
    (r'^(?P<key_name>[\w-]+)$', 'detail'),
#    (r'^(?P<page>[^\.^/]+\.html)$', 'page'),
)



    
