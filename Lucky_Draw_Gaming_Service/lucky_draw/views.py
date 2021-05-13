from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import response
from rest_framework.response import Response
import uuid
from .models import *
from datetime import *
import random 
from django.utils import timezone


class Grofer_Event(viewsets.ViewSet):

        def generateticket(self,request):
           # import ipdb; ipdb.set_trace()
            response = {}
            username = request.data["username"]
            try:
                check_user = User.objects.get(username = username)
                ticket_number = uuid.uuid1()
                new_ticket = Ticket(user = check_user, number = ticket_number)
                new_ticket.save()
                response["success"] = True
                response["ticket"] = ticket_number
            except:
                response["success"] = False
                response["message"] = "The entered username does not exist"
            return Response(data = response, content_type="application/json")

        def participate(self, request):
            #import ipdb; ipdb.set_trace()
            response = {}
            username = request.data["username"]
            ticket_number = request.data["ticket_number"]
            event_name = request.data["event_name"]

            #user should be a valid user
            try:
                check_user = User.objects.get(username = username)
            except:
                response["success"] = False
                response["message"] = "The entered username does not exist"
                return Response(data = response, content_type="application/json")

            #event_name should be a valid event
            try:
                check_event = Event.objects.get(event_name=event_name)
            except:
                response["success"] = False
                response["message"] = "The requested event does not exist"
                return Response(data = response, content_type="application/json")

            #A user cannot take part in an event again
            try:
                already_took_part = Ticket.objects.get(user = check_user, event_name = event_name)
                response["success"] = False
                response["message"] = "The requested user cannot take part in the same event again"
                return Response(data = response, content_type="application/json")
            except:
                pass

            #ticket number should be valid, should not be used before in any event and should belong to the requested user
            try:
                check_ticket = Ticket.objects.get(number = ticket_number)
                if(check_ticket.event_name):
                    response["success"] = False
                    response["message"] = "The ticket has already been used"
                    return Response(data = response, content_type="application/json")
                if(check_ticket.user != check_user):
                    response["success"] = False
                    response["message"] = "The ticket does not belong to the requested user"
                    return Response(data = response, content_type="application/json")
            except: 
                response["success"] = False
                response["message"] = "The entered ticket number does not exist"
                return Response(data = response,content_type="application/json")

            check_ticket.event_name = event_name
            check_ticket.save()
            response["success"] = True
            return Response(data = response, content_type="application/json")

        def upcoming_event(self, request):
            response = {}
            try:
                result = Event.objects.filter(
                start_time__gte = datetime.today()
                ).order_by(
                'start_time'
                ).first()
                response["success"] = True
                response["event_name"] = result.event_name
            except:
                response["success"] = False
                response["message"] = "No upcoming event"
            return Response(data = response, content_type="application/json")

            
