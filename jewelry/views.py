from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.conf import settings
import csv
import os
import logging

class JewelryItem:
    def __init__(self, **kwargs):
        self.year = kwargs.get('year', '')
        self.name = kwargs.get('name', '')
        self.key_name = kwargs.get('key_name', '')
        self.material = kwargs.get('material', '')
        self.size = kwargs.get('size', '')
        self.style = kwargs.get('style', '')
        self.image = kwargs.get('image', '')
        self.pk = kwargs.get('key_name', '')  # For compatibility
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Return the URL for this jewelry item's detail page"""
        return f'/jewelry/{self.pk}/'

def load_jewelry_data():
    """Load jewelry data from CSV file"""
    csv_path = os.path.join(settings.MEDIA_ROOT, 'jewelry', 'jewelry.csv')
    jewelry_items = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('name'):  # Skip empty rows
                    jewelry_items.append(JewelryItem(**row))
    except Exception as e:
        logging.error(f'Error loading jewelry CSV: {e}')
    
    return jewelry_items

def get_jewelry_by_key(key_name):
    """Get a specific jewelry item by key_name"""
    items = load_jewelry_data()
    for item in items:
        if item.key_name == key_name:
            return item
    return None

def filter_jewelry_by_style(style):
    """Filter jewelry items by style"""
    items = load_jewelry_data()
    return [item for item in items if item.style == style]

def index(request):
    j = sorted(load_jewelry_data(), key=lambda x: x.name)
    return render(request, 'jewelry/index.html', {'jewelry': j})

def page(request, page): 
    j = sorted(load_jewelry_data(), key=lambda x: x.name)
    return render(request, f'jewelry/{page}', {'jewelry': j})

def list(request):
    j = sorted(load_jewelry_data(), key=lambda x: x.name)
    return render(request, 'jewelry/list.html', {'jewelry': j})
 
def pendants(request):
    j = filter_jewelry_by_style('pendant')
    return render(request, 'jewelry/table.html', {'jewelry': j, 'sidemenu': 'pendants'})

def earrings(request):
    j = filter_jewelry_by_style('earring')
    return render(request, 'jewelry/table.html', {'jewelry': j, 'sidemenu': 'earrings'})

def pins(request):
    j = filter_jewelry_by_style('pin')
    return render(request, 'jewelry/table.html', {'jewelry': j, 'sidemenu': 'pins'})

def other(request):
    j = filter_jewelry_by_style('bracelet')
    return render(request, 'jewelry/table.html', {'jewelry': j, 'sidemenu': 'other'})

def detail(request, key):
    j = get_jewelry_by_key(key)
    if not j:
        raise Http404("Jewelry item not found")
    return render(request, 'jewelry/jewelry.html', {'jewel': j})


