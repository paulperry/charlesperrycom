from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context
from jewelry import models
import bforms
from django.shortcuts import render_to_response
from django.views.generic.simple import redirect_to
import csv
import urllib
import logging

def index(request):
    j = models.Jewelry.all().order('name')
    return render_to_response('jewelry/index.html', {'jewelry': j})

def page(request, page): 
    j = models.Jewelry.all().order('name')
    return render_to_response('jewelry/' + page, {'jewelry': j})

def list(request):
    j = models.Jewelry.all().order('name')
    return render_to_response('jewelry/list.html', {'jewelry': j})
 
def pendants(request):
    j = models.Jewelry.all().filter('style = ', 'pendant')
    return render_to_response('jewelry/table.html', {'jewelry': j}, Context({'sidemenu': 'pendants'}))

def earrings(request):
    j = models.Jewelry.all().filter('style = ', 'earring')
    return render_to_response('jewelry/table.html', {'jewelry': j}, Context({'sidemenu': 'earrings'}))

def pins(request):
    j = models.Jewelry.all().filter('style = ', 'pin')
    return render_to_response('jewelry/table.html', {'jewelry': j}, Context({'sidemenu': 'pins'}))

def other(request):
    j = models.Jewelry.all().filter('style = ', 'bracelet')
    return render_to_response('jewelry/table.html', {'jewelry': j}, Context({'sidemenu': 'other'}))

def detail(request, key):
    j = models.Jewelry.get_by_key_name(key)
    if j:
        return render_to_response('jewelry/jewelry.html', {'jewel': j})
    else:
        raise Http404
#        return redirect_to(request, '/jewelry/') # index(request)

def build(request):
    # dump the model DB
    for a in models.Jewelry.all():
        a.delete()
    # open the CSV file
#    f = open('/media/jewelry/jewelry.csv', 'rb') 
    f = urllib.urlopen('http://www.charlesperry.com/media/jewelry/jewelry.csv') 

    reader = csv.reader(f)
    titles = reader.next()
    reader = csv.DictReader(f, titles)

    for row in reader:
        p = models.Jewelry(name = row['name']
                          ,material = row['material']
                          ,size = row['size']
                          ,style = row['style']
                          ,image = row['image']
                          ,key_name = row['key_name']
                          )
        p.save()

    bind()

    return list(request)

def bind():
    js = models.Jewelry.all().order('name')
    lst = []
    for j in js:
        lst.append(str(j))

    j = models.Jewelry.all().filter('__key__ >', j.key()).get()

    for i, j in enumerate(js):
         if i == 0:
              j.next = str(lst[1])
              j.prev = str(lst[len(lst)-1])
         elif i == len(lst)-1:
              j.next = str(lst[0])
              j.prev = str(lst[i-1])
         else:
              j.next = str(lst[i+1])
              j.prev = str(lst[i-1])
         j.save()

    return

