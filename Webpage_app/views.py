from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Contact

def home(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {'current_time': now})

def contact(request):
    return render(request, 'contact.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = Contact(name=name, email=email)
        contact.save()
        return HttpResponse(f'Thank you {name}, we will contact you at {email}.')
    return HttpResponse('Invalid request.')

def display_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
