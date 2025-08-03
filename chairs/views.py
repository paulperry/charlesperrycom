from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist

def index(request):
    return render(request, 'chairs/index.html')

def page(request, page): 
    try:
        return render(request, f"chairs/{page}.html")
    except TemplateDoesNotExist:
        raise Http404

def detail(request, key):
    # Simple static chair detail view without database
    # The template will handle showing chair details based on the key
    return render(request, 'chairs/chair.html', {'key': key})



