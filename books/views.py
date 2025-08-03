# books/views.py
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist

def index(request):
    return render(request, 'books/index.html')

def page(request, page): 
    try:
        return render(request, f"books/{page}.html")
    except TemplateDoesNotExist:
        raise Http404




