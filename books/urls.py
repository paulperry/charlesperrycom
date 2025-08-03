# books/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='books_index'),
    re_path(r'^(?P<page>[\w-]+)$', views.page, name='books_page'),
]



    
