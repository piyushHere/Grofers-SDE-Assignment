from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
import uuid
from rest_framework import response
from .models import *
from datetime import *
from django.utils import timezone
from rest_framework.response import Response


class Grofer_Event(viewsets.ViewSet):

        def generateticket(self,request):
            username = request.data["username"]
            try:
                check_user = User.objects.get(username = username)
                ticket_number = uuid.uuid1()
                new_ticket = Ticket(user = check_user, number = ticket_number)
                new_ticket.save()
                response["success"] = True
                response["ticket"] = new_ticket
            except:
                response["success"] = False
                response["message"] = "The entered Email ID is not registered"
            return Response(data = response, content_type="application/json")

            

