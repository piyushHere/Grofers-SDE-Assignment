from django.contrib import admin
from .models import User,Ticket,Event
# Register your models here.

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Event)