from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generateticket', views.generate_ticket, name='generate_ticket'),
    
]