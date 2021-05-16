from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import response
from rest_framework.response import Response
import uuid
from .models import *
from datetime import *
import random 
from django.utils import timezone
from celery.schedules import crontab


class Grofer_Event(viewsets.ViewSet):

        def generateticket(self,request):
            response = {}
            username = request.data["username"]
            # If the user is a registered user, only then they can generate a new ticket
            try:
                check_user = User.objects.get(username = username)
                ticket_number = uuid.uuid1()
                new_ticket = Ticket(user = check_user, number = ticket_number)
                new_ticket.save()
                response["success"] = True
                response["ticket"] = ticket_number
            # If the user does not exist in our database then we will send the respose accordingly
            except:
                response["success"] = False
                response["message"] = "The entered username does not exist"
            return Response(data = response, content_type="application/json")

        def participate(self, request):
            response = {}
            # We will first take the details required to participate in an event
            username = request.data["username"]
            ticket_number = request.data["ticket_number"]
            event_name = request.data["event_name"]

            # User should be a registered user
            try:
                check_user = User.objects.get(username = username)
            except:
                response["success"] = False
                response["message"] = "The entered username does not exist"
                return Response(data = response, content_type="application/json")

            #event_name should be a valid event
            try:
                check_event = Event.objects.get(event_name=event_name)
                if(check_event.end_time<timezone.now()):
                    response["success"] = False
                    response["message"] = "The requested event is over now"
                    return Response(data = response, content_type="application/json")
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
                # Query the next event that occurs after current time
                result = Event.objects.filter(
                start_time__gte = datetime.today()
                ).order_by(
                'start_time'
                ).first()
                response["success"] = True
                response["event_name"] = result.event_name
                response["event_prize"] = result.event_prize
            except:
                response["success"] = False
                response["message"] = "No upcoming event"
            return Response(data = response, content_type="application/json")

        def last_week_winners(self,request):
            response = {}
            # Query the event objects that happened in the past week
            starttime = datetime.today() - timedelta(days = 7)
            endtime = datetime.today() - timedelta(days = 1)
            last_week_events = Event.objects.filter(end_time__range = [starttime, endtime])
            if not last_week_events:
                response["message"] = "No events happened in the last week"
                return Response(data = response, content_type="application/json")

            for daily_event in last_week_events:
                response[str(daily_event.event_name)] = daily_event.event_winner
            return Response(data = response, content_type="application/json")

        
        # Function to update winners of contest everyday at 12 am
        def update_winner(self, events):
            for single_event in events:
                #Find possible candidates that can win and choose a winner randomly
                participants = Ticket.objects.get(event_name = single_event.event_name)
                winner_ticket = random.choice(participants)
                winner_user = winner_ticket.user
                #Update this user in event record
                single_event.event_winner = winner_user.name
                single_event.save()





            
