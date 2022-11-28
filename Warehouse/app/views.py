from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/home.html')


def products(request):
    products_list = Product.objects.all()
    context = {'products': products_list}
    return render(request, 'app/products.html', context)


@login_required(login_url='login')
def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app/create-product.html', context)


@login_required(login_url='login')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'app/create-product.html', context)


@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'object': product}
    return render(request, 'app/delete-template.html', context)


def category(request):
    context = {
        'page': 'category',
        'number': 11,
    }
    return render(request, 'app/category.html', context)


def single_category(request, pk):
    return render(request, 'app/single-category.html', {'id': pk})
