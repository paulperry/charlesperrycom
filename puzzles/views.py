# puzzles/views.py
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist
from puzzles import models
import bforms

def index(request):
    return render_to_response('puzzles/index.html')

def page(request, page): 
    try:
        return direct_to_template(request, template="puzzles/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404

#    return render_to_response('puzzles/' + page)

def results(request, puzzle):
    pz = models.Puzzle.all().filter('name = ', puzzle)
    payload = dict(puzzles = pz)
    return render_to_response('puzzles/table.html', payload)

def puzzle_detail(request, puzzle_key):
    puzzle = models.Puzzle.get(puzzle_key)
    payload = dict(puzzle = puzzle)
    return render_to_response('puzzles/puzzle.html', payload)

def list(request):
    puzzles = models.Puzzle.all()
    payload = dict(puzzles = puzzles)
    return render_to_response('puzzles/list.html', payload)
 



