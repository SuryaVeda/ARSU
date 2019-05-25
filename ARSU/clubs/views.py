from django.shortcuts import render, redirect
from .models import Clubs, Categories, Events
from home.decorators import student_required, cr_required
from .forms import EventForms, ClubsForm, CategoriesForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def clubs(request):
    template_name = 'clubs/clubs.html'
    clubs = Clubs.objects.order_by('pk')
    return render(request, template_name, {'clubs':clubs})
@login_required
@cr_required
def posts(request, id):
    template_name = 'accounts/table.html'
    form = EventForms()
    if request.method == 'POST':
        form = EventForms(request.POST, request.FILES)
        if form.is_valid():
           form = form.save(commit=False)
           form.post = Categories.objects.get(pk=id)
           form.save()
           return redirect('clubs:clubs')
    else:
        form = EventForms()
    return render(request, template_name, {'form':form})
@login_required
@cr_required
def addClub(request):
    template_name = 'accounts/table.html'
    form = ClubsForm()
    if request.method == 'POST':
        form = ClubsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clubs:clubs')
        else:
            form = ClubsForm()
    return render(request, template_name, {'form':form})
@login_required
@cr_required
def addCategories(request, id):
    template_name = 'accounts/table.html'
    form = CategoriesForm()
    if request.method == 'POST':
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
           form = form.save(commit=False)
           form.post = Clubs.objects.get(pk=id)
           form.save()
           return redirect('clubs:clubs')
    else:
        form = CategoriesForm()
    return render(request, template_name, {'form':form})
@login_required
def newClub(request, id):
    template_name ='clubs/new.html'
    clubs = Clubs.objects.order_by('pk')
    club = Clubs.objects.get(pk=id)
    details = Categories.objects.filter(post = club).order_by('pk')
    events = Events.objects.order_by('pk')
    context = {'club':club, 'details':details, 'events':events, 'clubs':clubs}
    return render(request, template_name, context)
@login_required
@cr_required
def event_delete(request,id):
    event = Events.objects.get(pk=id)
    event.delete()
    return redirect('clubs:clubs')
