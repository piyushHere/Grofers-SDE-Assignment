from .models import *
from datetime import *
from .views import *

def my_cron_job():
    events = Event.objects.filter(end_time = datetime.today())
    if events:
        Grofer_Event.update_winner(events)