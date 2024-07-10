from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('contacts/', views.display_contacts, name='display_contacts'),
]
