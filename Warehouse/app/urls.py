from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-product', views.create_product, name='create-product'),
    path('update-product/<str:pk>/', views.update_product, name='update-product'),
    path('home/<str:pk>', views.single_category, name='category'),
]