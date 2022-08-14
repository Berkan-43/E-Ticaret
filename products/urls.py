from turtle import home
from django.urls import path
from products.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('basket/', basket, name='basket'),
    path('product-add/', product_add, name='add'),
]