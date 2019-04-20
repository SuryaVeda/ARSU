from django.shortcuts import render, redirect
from clubs.models import Events
# Create your views here.
def events(request):
    template_name = 'events/events.html'
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'events':events})
def details(request):
    template_name = 'events/details.html'
    return render(request, template_name)
