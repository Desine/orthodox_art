from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404


def master(request):
    return render(request, 'master.html')









def catalog(request):
    products = Product.objects.all().prefetch_related(
        'images',
        'types',
        'sizes',
        'materials'
    )
    return render(request, 'catalog.html', {'products': products})


def product(request, pk):
    product = get_object_or_404(
        Product.objects.prefetch_related(
            'images',
            'types',
            'sizes',
            'materials'
        ),
        pk=pk
    )
    return render(request, 'product.html', {'product': product})









def life(request):
    return render(request, 'life.html')

def contacts(request):
    return render(request, 'contacts.html')