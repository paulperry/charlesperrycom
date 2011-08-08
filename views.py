from django.http import HttpResponse, HttpResponseRedirect
import bforms
from django.shortcuts import render_to_response

def index(request):
    return render_to_response(request, 'index.html')


