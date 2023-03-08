from django.urls import path
from .views import home, about, contact, tours

app_name='my_weblog'

urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path('contact', contact , name='contact'),
    path('tours', tours , name='tours'),
]