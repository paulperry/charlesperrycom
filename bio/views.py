# bio/views.py
#
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist
from bforms import ContactForm, SubscribeForm
import bforms

def index(request):
    return render_to_response('bio/bio.html')

def page(request, page):
    try:
        return direct_to_template(request, template="bio/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404

#    return render_to_response('bio/' + page)

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['paul@charlesperry.com']
            if cc_myself:
                recipients.append(email)
            sender = 'paulperry@gmail.com'
            to = recipients
            subject = subject
            body += name
            body += ' - '
            body += email
            body += ' - '
            body = message

            try:
                from google.appengine.api import mail
                mail.send_mail(sender, to, subject, body)
            except:
                import logging
                err = 'failed to send email: '
                err += sender
                err += ' - '
                err += err.join(to)
                err += ' - '
                err += subject
                err += ' - '
                err += body
                err += ' ... '
                logging.error(err)
            return HttpResponseRedirect('/bio/thanks.html')
    else:
        form = bforms.ContactForm() # An unbound form
    return render_to_response('bio/contact.html', {'form': form})

def subscribe(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SubscribeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = 'charlesperry mail list add ' + email
            body = 'please add ' + name + ' ' + email + ' to the newsletter list'
            to = ['paul@charlesperry.com']
            sender = 'paulperry@gmail.com'

            try:
                from google.appengine.api import mail
                mail.send_mail(sender, to, subject, body)
            except:
                import logging
                err = 'failed to send email: '
                err += sender
                err += ' - '
                err += err.join(to)
                err += ' - '
                err += subject
                err += ' - '
                err += body
                err += ' ... '
                logging.error(err)
 
            return HttpResponseRedirect('/bio/thanks.html') 
    else:
        form = bforms.ContactForm() # An unbound form
    return render_to_response('bio/contact.html', {'form': form})
