from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


def user(request):
    return render(request, 'main.html')


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('products')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'user/login-register.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'User was successfully logged out')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # In case we want to manipulate this, eg. lowercase username
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User was created')

            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'An error has occured')

    context = {'page': page, 'form': form}
    return render(request, 'user/login-register.html', context)
