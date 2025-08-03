from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='jewelry_index'),
    path('pendants/', views.pendants, name='jewelry_pendants'),
    path('earrings/', views.earrings, name='jewelry_earrings'),
    path('pins/', views.pins, name='jewelry_pins'),
    path('other/', views.other, name='jewelry_other'),
    re_path(r'^(?P<key>[\w-]+)/$', views.detail, name='jewelry_detail'),
]
