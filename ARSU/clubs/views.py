from django.shortcuts import render, redirect
from .models import Clubs, details, Events
from .forms import EventForms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def clubs(request):
    template_name = 'clubs/clubs.html'
    clubs = Clubs.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs})
@login_required
def sports(request):
    template_name = 'clubs/sports.html'
    clubs = Clubs.objects.order_by('pk')
    detail = details.objects.order_by('pk')
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs, 'detail':detail, 'events':events})
@login_required
def cultural(request):
    template_name = 'clubs/cultural.html'
    clubs = Clubs.objects.order_by('pk')
    detail = details.objects.order_by('pk')
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs, 'detail':detail, 'events':events})
@login_required
def FineArts(request):
    template_name = 'clubs/FineArts.html'
    clubs = Clubs.objects.order_by('pk')
    detail = details.objects.order_by('pk')
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs, 'detail':detail, 'events':events})
@login_required
def literary(request):
    template_name = 'clubs/literary.html'
    clubs = Clubs.objects.order_by('pk')
    detail = details.objects.order_by('pk')
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs, 'detail':detail, 'events':events})
@login_required
def magazine(request):
    template_name = 'clubs/magazine.html'
    clubs = Clubs.objects.order_by('pk')
    detail = details.objects.order_by('pk')
    events = Events.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs, 'detail':detail, 'events':events})
@login_required
def posts(request):
    template_name = 'clubs/EventForm.html'
    form = EventForms()
    if request.method == 'POST':
        form = EventForms(request.POST)
        if form.is_valid():
           form = form.save(commit=False)
           form.user = request.user
           form.save()
           return redirect('clubs:clubs')
    else:
        form = EventForms()
        return render(request, template_name, {'form':form})
