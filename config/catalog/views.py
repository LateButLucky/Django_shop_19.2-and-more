from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact, Product, Category


def home(request):
    return render(request, 'home.html')


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, message=message)
    return render(request, 'contact.html')
