# puzzles/views.py
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.conf import settings
import csv
import os
import logging

def index(request):
    return render(request, 'puzzles/index.html')

def page(request, page): 
    try:
        return render(request, f"puzzles/{page}.html")
    except TemplateDoesNotExist:
        raise Http404

class PuzzleItem:
    def __init__(self, **kwargs):
        self.year = kwargs.get('year', '')
        self.name = kwargs.get('name', '')
        self.material = kwargs.get('material', '')
        self.location = kwargs.get('location', '')
        self.size = kwargs.get('size', '')
        self.image = kwargs.get('image', '')
        self.pk = self.name.lower().replace(' ', '-').replace('.', '')  # For compatibility
        
    def __str__(self):
        return self.name

def load_puzzle_data():
    """Load puzzle data from CSV file"""
    csv_path = os.path.join(settings.MEDIA_ROOT, 'puzzles', 'puzzles.csv')
    puzzle_items = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('name'):  # Skip empty rows
                    puzzle_items.append(PuzzleItem(**row))
    except Exception as e:
        logging.error(f'Error loading puzzles CSV: {e}')
    
    return puzzle_items

def get_puzzle_by_name(name):
    """Get a specific puzzle item by name"""
    items = load_puzzle_data()
    for item in items:
        if item.name.lower() == name.lower():
            return item
    return None

def get_puzzle_by_key(key):
    """Get a specific puzzle item by key"""
    items = load_puzzle_data()
    for item in items:
        if item.pk == key:
            return item
    return None

def results(request, puzzle):
    items = load_puzzle_data()
    pz = [item for item in items if item.name.lower() == puzzle.lower()]
    return render(request, 'puzzles/table.html', {'puzzles': pz})

def puzzle_detail(request, puzzle_key):
    puzzle = get_puzzle_by_key(puzzle_key)
    if not puzzle:
        raise Http404("Puzzle not found")
    return render(request, 'puzzles/puzzle.html', {'puzzle': puzzle})

def list(request):
    puzzles = load_puzzle_data()
    return render(request, 'puzzles/list.html', {'puzzles': puzzles})
 



