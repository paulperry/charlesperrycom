# sculpture/views.py
#
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.conf import settings
import csv
import os
import logging

class SculptureItem:
    def __init__(self, **kwargs):
        self.year = kwargs.get('year', '')
        self.name = kwargs.get('name', '')
        self.location = kwargs.get('location', '')
        self.address = kwargs.get('address', '')
        self.city = kwargs.get('city', '')
        self.state = kwargs.get('state', '')
        self.country = kwargs.get('country', '')
        self.material = kwargs.get('material', '')
        self.size = kwargs.get('size', '')
        self.style = kwargs.get('style', '')
        self.image = kwargs.get('image', '')
        self.key_name = kwargs.get('key_name', '')
        self.lat = kwargs.get('lat', '')
        self.lon = kwargs.get('lon', '')
        self.geolink = kwargs.get('geolink', '')
        self.visible = kwargs.get('visible', '')
        self.pk = kwargs.get('key_name', '')  # For compatibility
        
        # Navigation fields (will be computed)
        self.prev_style = ''
        self.next_style = ''
        self.prev_material = ''
        self.next_material = ''
    
    def __str__(self):
        return self.name or self.key_name
    
    def get_absolute_url(self):
        """Return the URL for this sculpture's detail page"""
        return f'/sculpture/{self.key_name}/'

def load_sculpture_data():
    """Load sculpture data from CSV file"""
    csv_path = os.path.join(settings.MEDIA_ROOT, 'sculpture', 'art.csv')
    sculpture_items = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('name'):  # Skip empty rows
                    sculpture_items.append(SculptureItem(**row))
    except Exception as e:
        logging.error(f'Error loading sculpture CSV: {e}')
    
    return sculpture_items

def get_sculpture_by_key(key_name):
    """Get a specific sculpture item by key_name"""
    items = load_sculpture_data()
    for item in items:
        if item.key_name == key_name:
            return item
    return None

def filter_sculpture_by_style(style):
    """Filter sculpture items by style"""
    items = load_sculpture_data()
    return [item for item in items if item.style == style and item.image]

def filter_sculpture_by_material(materials):
    """Filter sculpture items by material(s)"""
    items = load_sculpture_data()
    if isinstance(materials, str):
        materials = [materials]
    return [item for item in items if item.material in materials and item.image]


def index(request):
    return render(request, 'index.html')

def page(request, page): 
    try:
        return render(request, f"sculpture/{page}.html")
    except TemplateDoesNotExist:
        raise Http404

def index_style(request):
    arts = sorted(load_sculpture_data(), key=lambda x: x.name)
    response = render(request, 'sculpture/index.html', {'arts': arts})
    response.set_cookie('nav_path', 'style')
    return response


def style(request):
    return render(request, 'sculpture/style.html')

def material(request):
    response = render(request, 'sculpture/material.html', {'sideselection': 'material'})
    response.set_cookie('nav_path', 'material')
    return response

def art_style(request, art_style):
    arts = filter_sculpture_by_style(art_style)
    response = render(request, 'sculpture/table.html', {'arts': arts, 'sideselection': 'style', 'subselection': art_style})
    response.set_cookie('nav_path', 'style')
    return response

def material_view(request, art_material):
    if art_material == 'aluminum':
        arts = filter_sculpture_by_material('Aluminum')
        subselection = 'aluminum'
    elif art_material == 'bronze':
        arts = filter_sculpture_by_material(['Bronze', 'Brass'])
        subselection = 'bronze'
    elif art_material == 'steel':
        arts = filter_sculpture_by_material('Steel')
        subselection = 'steel'
    elif art_material == 'stainlesssteel':
        arts = filter_sculpture_by_material('Stainless Steel')
        subselection = 'stainlesssteel'
    elif art_material == 'other':
        arts = filter_sculpture_by_material(['Granite', 'Marble', 'Plexiglas', 'Wood'])
        subselection = 'other'
    else:
        arts = []
        subselection = art_material
        
    response = render(request, 'sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': subselection})
    response.set_cookie('nav_path', 'material')
    return response


# def art_detail(request, art_key):
#     art = models.Sculpture.get(art_key)
#     return render_to_response('sculpture/details.html', {'art': art})

def detail(request, key_name):
    art = get_sculpture_by_key(key_name)
    if not art:
        raise Http404("Sculpture not found")

    cookie = ''
    prev = key_name
    next = key_name
    if 'nav_path' in request.COOKIES:
         cookie = request.COOKIES['nav_path']
         if cookie == 'material':
              prev = art.prev_material
              next = art.next_material
         else:
              prev = art.prev_style
              next = art.next_style

    response = render(request, 'sculpture/details.html', {'art': art, 'prev': prev, 'next': next})
    response.set_cookie('nav_path', cookie)
    return response




def all(request):
    arts = [item for item in load_sculpture_data() if item.image]
    return render(request, 'sculpture/table.html', {'arts': arts})
 
def list(request):
    arts = sorted(load_sculpture_data(), key=lambda x: x.name)
    return render(request, 'sculpture/list.html', {'arts': arts})

def flush(request):
    """No-op since we're using file-based data"""
    return HttpResponse("No database to flush - using CSV files directly", content_type='text/plain')


def genkml(request):
    """Generate KML file for Google Maps"""
    arts = sorted(load_sculpture_data(), key=lambda x: x.name)
    response = render(request, 'sculpture/perry.kml', {'arts': arts, 'request': request})
    response['Content-Type'] = 'application/vnd.google-earth.kml+xml'
    response['Content-Disposition'] = 'attachment; filename="perry.kml"'
    return response

def tour(request):
    arts = [item for item in load_sculpture_data() if item.visible == 'y' and item.geolink]
    return render(request, 'sculpture/tour.html', {'arts': arts})

