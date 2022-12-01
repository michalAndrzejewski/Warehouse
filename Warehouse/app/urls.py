from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.products, name='products'),
    path('create-product/', views.create_product, name='create-product'),
    path('update-product/<str:pk>/', views.update_product, name='update-product'),
    path('delete-template/<str:pk>/', views.delete_product, name='delete-product'),

    path('products/csv/', views.product_csv, name='products-csv'),

    path('categories/', views.categories, name='categories'),
    path('create-category/', views.create_category, name='category-create'),
    path('update-category/<str:pk>/', views.update_category, name='category-update'),
    path('category-delete/<str:pk>/', views.delete_category, name='delete-category'),

]