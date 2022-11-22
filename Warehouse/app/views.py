from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

cars = [
    {
        'make': 'Toyota',
        'model': 'Corolla',
        'id': 1,
    },
    {
        'make': 'Fiat',
        'model': 'Bravo',
        'id': 2,
    },
]


def home(request):
    return render(request, 'app/home.html')


def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app/product.html', context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app/product.html', context)

def category(request):
    context = {
        'page': 'category',
        'number': 11,
        'cars': cars
    }
    return render(request, 'app/category.html', context)


def single_category(request, pk):
    return render(request, 'app/single-category.html', {'id': pk})
