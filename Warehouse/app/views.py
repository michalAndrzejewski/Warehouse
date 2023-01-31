from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, CategoryForm
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from .utils.csv_export import product_csv


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
            return redirect('products')

    context = {'form': form}
    return render(request, 'app/product-create.html', context)


@login_required(login_url='login')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    print(product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        print(product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'app/product-create.html', context)


@login_required(login_url='login')
def delete_product(request, pk):
    print('delete product')
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'object': product}
    return render(request, 'app/product-delete.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'app/category.html', context)


@login_required(login_url='login')
def create_category(request):
    form = CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {'form': form}
    return render(request, 'app/category-create.html', context)


@login_required(login_url='login')
def update_category(request, pk):
    print('category updating')
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        print('category post data')
        if form.is_valid():
            form.save()
            return redirect('categories')

    context = {'form': form}
    return render(request, 'app/category-create.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    context = {'object': category}
    return render(request, 'app/category-delete.html', context)


def generate_product_csv(response):
    return product_csv(response)


# comment from dev