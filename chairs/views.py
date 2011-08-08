from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist
import models
import bforms

def index(request):
    return render_to_response('chairs/index.html')

def page(request, page): 
    try:
        return direct_to_template(request, template="chairs/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404

#    return render_to_response('chairs/' + page)

def detail(request, key):
    chair = models.Chair.get(key)
    return render_to_response('chairs/chair.html', {'chair': chair})



