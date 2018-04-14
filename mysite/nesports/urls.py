from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.images, name='images'),
    path('patriots', views.patriots, name='patriots'),
    path('celtics', views.celtics, name='celtics'),
    path('bruins', views.bruins, name='bruins'),
    path('redsox', views.redsox, name='redsox')
    ]