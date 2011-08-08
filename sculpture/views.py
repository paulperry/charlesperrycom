# sculpture/views.py
#
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist
from minidetector import detect_mobile
from sculpture import models
import bforms
import csv
import urllib
import logging

# check_mobile
# From: http://stackoverflow.com/questions/164427/change-django-templates-based-on-user-agent
# https://github.com/shelfworthy/minidetector
# Http://tech.agilitynerd.com/?tag=minidetector
#
def check_mobile(request, template_name):
#     if request.mobile:
#          return 'mobile-%s'%template_name
     return template_name

def index(request):
    return render_to_response('index.html')
#    return render_to_response(check_mobile(request, 'index.html'))

def page(request, page): 
    try:
        return direct_to_template(request, template="sculpture/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404

def index_style(request):
    arts = models.Sculpture.all().order('name')
    response = render_to_response('sculpture/index.html', {'arts': arts})
    response.set_cookie('nav_path', 'style')
    return response

def create(request):
    if request.method == 'GET':
        artform = bforms.SculptureForm()
    if request.method == 'POST':
        artform = bforms.SculptureForm(request.POST)
        if artform.is_valid():
            art = artform.save()
            return HttpResponseRedirect(art.get_absolute_url())
    return render_to_response('sculpture/create.html', {'artform': artform})

def style(request):
    return render_to_response('sculpture/style.html')

def material(request):
#    arts = models.Sculpture.all().order('name')
#    response = render_to_response('sculpture/material.html', {'arts': arts, 'sideselection': 'material'})
    response = render_to_response('sculpture/material.html', {'sideselection': 'material'})
    response.set_cookie('nav_path', 'material')
    return response

def art_style(request,art_style):
    arts = models.Sculpture.all().filter('style = ',art_style).filter('image != ', '')
    response = render_to_response('sculpture/table.html', {'arts': arts, 'sideselection': 'style', 'subselection': art_style})
    response.set_cookie('nav_path', 'style')
    return response

def aluminum(request, art_material):
    arts = models.Sculpture.all().filter('material = ', 'Aluminum').filter('image != ', '')
    response =  render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'aluminum'})
    response.set_cookie('nav_path', 'material')
    return response

def bronze(request, art_material):
    materials =  ['Bronze', 'Brass']
    arts = models.Sculpture.gql("WHERE material IN :1 AND image != ''", materials)
    response = render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'bronze'})
    response.set_cookie('nav_path', 'material')
    return response

def granite(request, art_material):
    arts = models.Sculpture.all().filter('material = ', 'Granite').filter('image != ', '')
    response = render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'granite'})
    response.set_cookie('nav_path', 'material')
    return response

def other(request, art_material):
    materials =  ['Granite', 'Marble', 'Plexiglas', 'Wood']
    arts = models.Sculpture.gql("WHERE material IN :1 AND image != ''", materials)
    response = render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'mother'})
    response.set_cookie('nav_path', 'material')
    return response

def steel(request, art_material):
    arts = models.Sculpture.all().filter('material = ', 'Steel').filter('image != ', '')
    response = render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'steel'})
    response.set_cookie('nav_path', 'material')
    return response

def stainlesssteel(request, art_material):
    arts = models.Sculpture.all().filter('material = ', 'Stainless Steel').filter('image != ', '')
    response = render_to_response('sculpture/mtable.html', {'arts': arts, 'sideselection': 'material', 'subselection': 'stainlesssteel'})
    response.set_cookie('nav_path', 'material')
    return response

# def art_detail(request, art_key):
#     art = models.Sculpture.get(art_key)
#     return render_to_response('sculpture/details.html', {'art': art})

def detail(request, key_name):
    art = models.Sculpture.get_by_key_name(key_name)
    if art == None:
         raise Http404

    cookie = ''
    prev = key_name
    next = key_name
    if 'nav_path' in request.COOKIES:
         cookie = request.COOKIES['nav_path']
#         logging.info('nav_path cookie: %s' % cookie)
         if cookie == 'material':
              prev = art.prev_material
              next = art.next_material
         else:
              prev = art.prev_style
              next = art.next_style

    response = render_to_response('sculpture/details.html',{'art':art,'prev':prev,'next':next})
    response.set_cookie('nav_path', cookie)
    return response


def detailx(request, key_name):
    art = models.Sculpture.get_by_key_name(key_name)
    from urlparse import urlparse
    try:
         o = request.META['HTTP_REFERER']
    except:
         o = None
    if o: 
         o = urlparse(request.META['HTTP_REFERER']).path
         from posixpath import basename, dirname
         prev = basename(o)
    else:
         prev = 'all'
# this version didn't fly
#    prev = models.Sculpture.all().filter('__key__ <', art.key()).get()
    next = models.Sculpture.all().filter('__key__ >', art.key()).get()
    return render_to_response('sculpture/details.html', {'art': art, 'prev': prev, 'next':next})


def all(request):
    arts = models.Sculpture.all().filter('image != ', '')
    return render_to_response('sculpture/table.html', {'arts': arts})
 
def list(request):
    arts = models.Sculpture.all().order('name')
    return render_to_response('sculpture/list.html', {'arts': arts})

def flush(model, limit = 1000):
    '''
    Flush all the objects associated with a Django model on GAE.
    From: http://groups.google.com/group/django-non-relational/browse_thread/thread/ad7766572334431e/902e2ab1385c7b00?lnk=raot
    '''
    from google.appengine.ext import db
    model  = type(model._meta.db_table, (db.Model,), {})
    cursor = None
    while True:
        q = model.all(keys_only = True)
        if cursor is not None: 
            q.with_cursor(cursor)
        keys = q.fetch(limit)
        if len(keys) == 0:
            logging.info('no object left for %s' % model)
            break
        logging.info('deleting %d objects...' % len(keys))
        db.delete(keys)
        cursor = q.cursor()
    return list(request)

import settings
def build(request):
    # dump the model DB
#    if models.Sculpture.all() == None:
#    flush(models.Sculpture)
    for a in models.Sculpture.all():
        a.delete()

    # open the CSV file
#    f = open(settings.MEDIA_ROOT + 'sculpture/art.csv', 'rb') 
    f = urllib.urlopen('http://www.charlesperry.com/media/sculpture/art.csv')

    reader = csv.reader(f)
    titles = reader.next()
    reader = csv.DictReader(f, titles)

    for row in reader:
        a = models.Sculpture(year = row['year']
                       ,name = row['name']
                       ,location = row['location']
                       ,address = row['address']
                       ,city = row['city']
                       ,state = row['state']
                       ,country = row['country']
                       ,material = row['material']
                       ,size = row['size']
                       ,style = row['style']
                       ,image = row['image']
                       ,lat = row['lat']
                       ,lon = row['lon']
                       ,geolink = row['geolink']
                       ,visible = row['visible']
                       ,key_name = row['key_name']
                       )
        a.save()

    return list(request)

def bind(request):
    arts = models.Sculpture.all().filter('style = ', 'ribbed').filter('image != ', '')
    bind_style(arts)
    arts = models.Sculpture.all().filter('style = ', 'planar').filter('image != ', '')
    bind_style(arts)
    arts = models.Sculpture.all().filter('style = ', 'topological').filter('image != ', '')
    bind_style(arts)
    arts = models.Sculpture.all().filter('style = ', 'solid').filter('image != ', '')
    bind_style(arts)

    arts = models.Sculpture.all().filter('material = ', 'Aluminum').filter('image != ', '')
    bind_material(arts)

    materials =  ['Bronze', 'Brass']
    arts = models.Sculpture.gql("WHERE material IN :1 AND image != ''", materials)
    bind_material(arts)

    materials =  ['Granite', 'Marble', 'Plexiglas', 'Wood']
    arts = models.Sculpture.gql("WHERE material IN :1 AND image != ''", materials)
    bind_material(arts)

    arts = models.Sculpture.all().filter('material = ', 'Steel').filter('image != ', '')
    bind_material(arts)

    arts = models.Sculpture.all().filter('material = ', 'Stainless Steel').filter('image != ', '')
    bind_material(arts)

    return list(request)


def bind_style(arts):    
    lst = []
    for art in arts:
         lst.append(str(art))

    for i, art in enumerate(arts):
         if i == 0:
              art.next_style = str(lst[1])
              art.prev_style = str(lst[len(lst)-1])
         elif i == len(lst)-1:
              art.next_style = str(lst[0])
              art.prev_style = str(lst[i-1])
         else:
              art.next_style = str(lst[i+1])
              art.prev_style = str(lst[i-1])
         art.save()

    return

def bind_material(arts):    
    lst = []
    for art in arts:
         lst.append(str(art))

    for i, art in enumerate(arts):
         if i == 0:
              art.next_material = str(lst[1])
              art.prev_material = str(lst[len(lst)-1])
         elif i == len(lst)-1:
              art.next_material = str(lst[0])
              art.prev_material = str(lst[i-1])
         else:
              art.next_material = str(lst[i+1])
              art.prev_material = str(lst[i-1])
         art.save()

    return

def genkml(request):
    '''
    <a href="http://groups.google.com/group/Google-Maps-How-Do-I/browse_thread/thread/56a50d52270f2503/feff48785b5a0fd6?lnk=gst&q=Last+Updated+by&pli=1">How to embed a map without the 'last updated' line in the item</a>
    '''
    arts = models.Sculpture.all().order('name')
    return render_to_response('sculpture/perry.kml',{'arts': arts, 'request': request}, mimetype="application/force-download")

def tour(request):
    arts = models.Sculpture.all().filter('visible = ', 'y').filter('geolink != ','')
    return render_to_response('sculpture/tour.html',{'arts': arts})

