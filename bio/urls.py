# bio/urls.py

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='bio_index'),
    path('contact/', views.contact, name='bio_contact'),
    re_path(r'^contact$', views.contact, name='bio_contact_no_slash'),
    path('subscribe/', views.subscribe, name='bio_subscribe'),
    re_path(r'^subscribe$', views.subscribe, name='bio_subscribe_no_slash'),
    re_path(r'^(?P<page>[\w-]+)$', views.page, name='bio_page'),
]

    
