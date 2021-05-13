from django.urls import path

from . import views

urlpatterns = [
    path('generateticket', views.Grofer_Event.as_view({"post":"generateticket"})),
    path('participate', views.Grofer_Event.as_view({"post":"participate"})),
    path('upcoming_event', views.Grofer_Event.as_view({"get":"upcoming_event"})),
    path('last_week_winners', views.Grofer_Event.as_view({"get":"last_week_winners"})),
]