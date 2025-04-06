from django.urls import path
from .views import *
urlpatterns = [
    path('', catalog, name='catalog'),
    path('master/', master, name='master'),
    path('catalog/', catalog, name='catalog'),
    path('life/', life, name='life'),
    path('contacts/', contacts, name='contacts'),
]
