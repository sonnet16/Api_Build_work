from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.getAllContact, name='list_contact'),
    path('create/', views.createContact, name='create'),
]