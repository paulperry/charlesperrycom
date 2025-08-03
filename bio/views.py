# bio/views.py
#
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from .bforms import ContactForm, SubscribeForm
from . import bforms

def index(request):
    return render(request, 'bio/bio.html')

def page(request, page):
    try:
        return render(request, f"bio/{page}.html")
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
            
            body = f"{name} - {email}\n\n{message}"

            # Send email using Django's email system
            try:
                from django.core.mail import send_mail
                from django.conf import settings
                
                # Use DEFAULT_FROM_EMAIL from settings as sender
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipients,
                    fail_silently=False
                )
                return HttpResponseRedirect('/bio/thanks.html')
            except Exception as e:
                import logging
                logging.error(f'Failed to send contact email: {e}')
                # In production, you might want to show an error page
                # For now, continue to thanks page even if email fails
                return HttpResponseRedirect('/bio/thanks.html')
    else:
        form = bforms.ContactForm() # An unbound form
    return render(request, 'bio/contact.html', {'form': form})

def subscribe(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SubscribeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = f'charlesperry mail list add {email}'
            body = f'please add {name} {email} to the newsletter list'
            to = ['paul@charlesperry.com']
            sender = 'paulperry@gmail.com'

            try:
                from django.core.mail import send_mail
                from django.conf import settings
                
                # Use DEFAULT_FROM_EMAIL from settings as sender
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=to,
                    fail_silently=False
                )
                return HttpResponseRedirect('/bio/thanks.html')
            except Exception as e:
                import logging
                logging.error(f'Failed to send subscription email: {e}')
                # In production, you might want to show an error page
                # For now, continue to thanks page even if email fails
                return HttpResponseRedirect('/bio/thanks.html') 
    else:
        form = bforms.SubscribeForm() # An unbound form
    return render(request, 'bio/subscribe.html', {'form': form})
