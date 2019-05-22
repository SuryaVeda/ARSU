from django.shortcuts import render, redirect
from clubs.models import Events
import datetime
from datetime import date, timedelta
# Create your views here.
def events(request):
    template_name = 'events/events.html'
    today = datetime.date.today()
    week = today + timedelta(days=7)
    events = Events.objects.filter(date__range = [today, week])
    return render(request, template_name, {'events':events})
def details(request):
    template_name = 'events/details.html'
    return render(request, template_name)
