# books/views.py
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist

def index(request):
    return render_to_response('books/index.html')

def page(request, page): 
    try:
        return direct_to_template(request, template="books/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404




