from django.urls import path

from . import views

urlpatterns = [
    path('generateticket', views.Grofer_Event.as_view({"post":"generateticket"})),
    path('participate', views.Grofer_Event.as_view({"post":"participate"})),
]