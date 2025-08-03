# sculpture urls.py
#
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_style, name='sculpture_index'),
    path('all/', views.all, name='sculpture_all'),
    path('tour/', views.tour, name='sculpture_tour'),
    re_path(r'^perry\.kml$', views.genkml, name='sculpture_kml'),
    path('list/', views.list, name='sculpture_list'),
    path('style/', views.style, name='sculpture_style'),
    path('map/', views.page, {'page': 'map'}, name='sculpture_map'),
    path('style/<str:art_style>/', views.art_style, name='sculpture_art_style'),
    path('material/', views.material, name='sculpture_material'),
    path('material/<str:art_material>/', views.material_view, name='sculpture_material_view'),
    path('slideshow/', views.page, {'page': 'slideshow'}, name='sculpture_slideshow'),
    path('slideshow', views.page, {'page': 'slideshow'}, name='sculpture_slideshow_no_slash'),
    re_path(r'^(?P<key_name>[\w-]+)/$', views.detail, name='sculpture_detail'),
]



    
