from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import Q
from home.models import Academic, NonAcademic, HospitalNews, CampusNews, batches, Carousel
from .forms import AcademicForm, NAcademicForm, HospitalNewsForm, CampusNewsForm
from django.contrib.auth.decorators import login_required
from .decorators import student_required
from notes.models import subject, sideHeading
from clubs.models import Clubs, details, Events
from accounts.models import User
from itertools import chain
# Create your views here.
@login_required
@student_required
def home(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        template_name = 'home/homePage.html'
        Aposts = Academic.objects.order_by('pk')
        NAposts = NonAcademic.objects.order_by('pk')
        Hposts = HospitalNews.objects.order_by('pk')
        Cposts = CampusNews.objects.order_by('pk')
        batch = batches.objects.order_by('pk')
        sliders = Carousel.objects.order_by('pk')
        users = User.objects.order_by('pk')
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        context = {'Aposts':Aposts, 'NAposts':NAposts, 'Hposts':Hposts, 'Cposts':Cposts, 'num_visits':num_visits, 'batch':batch, 'sliders':sliders, 'users':users}
        return render(request, template_name, context)


@login_required
@student_required

def AcadForm(request):
    template_name = 'home/AcadForm.html'
    if request.method =='POST':
       form = AcademicForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('home:home')
    else:
        form = AcademicForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def NAcadForm(request):
    template_name = 'home/NAcad.html'
    if request.method =='POST':
       form = NAcademicForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('home:home')
    else:
        form = NAcademicForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def HNForm(request):
    template_name = 'home/HN.html'
    if request.method =='POST':
       form = HospitalNewsForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('home:home')
    else:
        form = HospitalNewsForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def CNForm(request):
    template_name = 'home/CN.html'
    if request.method =='POST':
       form = CampusNewsForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('home:home')
    else:
        form = CampusNewsForm()
        return render(request, template_name, {'form':form})

@login_required
@student_required
def search(request):
    template_name = 'home/search.html'
    if request.method == 'GET':
        query = request.GET.get('q')
        submitButton = request.GET.get('submit')
        if query == "":
            return render(request, template_name)
        else:
            AcadResults = Academic.objects.filter(heading__icontains = query)
            NAcadResults = NonAcademic.objects.filter(heading__icontains = query)
            CampResults =  CampusNews.objects.filter(heading__icontains = query)
            HospResults = HospitalNews.objects.filter(heading__icontains = query)
            subjectResults = subject.objects.filter(heading__icontains = query)
            sideHeadingResults = sideHeading.objects.filter(heading__icontains = query)
            ClubsResults = Clubs.objects.filter(heading__icontains = query)
            DetailsResults = details.objects.filter(heading__icontains = query)
            EventsResults = Events.objects.filter(heading__icontains = query)
            Results = list(chain(AcadResults, NAcadResults, CampResults, HospResults,subjectResults,sideHeadingResults,ClubsResults,DetailsResults, EventsResults ))
            context = {'Results':Results, 'DetailsResults':DetailsResults}
            return render(request, template_name, context)

    else:
        return render(request, template_name)
