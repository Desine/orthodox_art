from django.shortcuts import render, redirect
from .models import *

def master(request):
    return render(request, 'master.html')

def catalog(request):
    products = Product.objects.all().prefetch_related(
        'images',
        'producttype_set__type',
        'productsize_set__size',
        'productmaterial_set__material'
    )
    return render(request, 'catalog.html', {'products': products})

def life(request):
    return render(request, 'life.html')

def contacts(request):
    return render(request, 'contacts.html')