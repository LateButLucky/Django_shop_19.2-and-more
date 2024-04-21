from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, message=message)
    return render(request, 'contact.html')


def home(request):
    return render(request, 'home.html')
