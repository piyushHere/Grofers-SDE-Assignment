from django.shortcuts import render
from django.http import HttpResponse
import uuid
from .models import *
from datetime import *
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import Response


class Grofer_Event:
def index(request):
    return HttpResponse("Welcome to Lucky Draw event, please register/sign in to begin participating in various events")


def generate_ticket(request):
