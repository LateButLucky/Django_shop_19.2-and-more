from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contact'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
]
