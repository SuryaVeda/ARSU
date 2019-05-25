from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import Q
from home.models import  NonAcademic, CampusNews, batches, Carousel, Schedule, Attendance, Results
from .forms import  NAcademicForm,  CampusNewsForm, ResultsForm, ScheduleForm, AttendanceForm
from django.contrib.auth.decorators import login_required
from .decorators import student_required, cr_required
from notes.models import subject, Lecture, Ebook, Paper
from clubs.models import Clubs, Categories, Events
from accounts.models import User
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
@student_required
def home(request):
    template_name = 'home/homePage.html'
    schedules = Schedule.objects.filter(batches = request.user.batch).order_by('pk')
    attendance = Attendance.objects.filter(batches = request.user.batch).order_by('pk')
    results = Results.objects.filter(batches = request.user.batch).order_by('pk')
    naca = NonAcademic.objects.order_by('pk')
    camp = CampusNews.objects.order_by('pk')
    batch = batches.objects.get(name=request.user.batch.name)
    sliders = Carousel.objects.order_by('pk')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = { 'schedules':schedules, 'attendance':attendance, 'num_visits':num_visits, 'batch':batch, 'sliders':sliders, 'results':results,'naca':naca, 'camp':camp }
    return render(request, template_name, context)
@login_required
@student_required
def schedule(request):
    template_name = 'home/AcadForm.html'
    form = ScheduleForm()
    if request.method =='POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.batches = request.user.batch
            form.save()
            return redirect('home:home')
        else:
            form = ScheduleForm()
    return render(request, template_name, {'form':form})


@login_required
@student_required
def attendance(request):
    template_name = 'home/AcadForm.html'
    form = AttendanceForm()
    if request.method =='POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.batches = request.user.batch
            form.save()
            return redirect('home:home')
        else:
            form = AttendanceForm()
    return render(request, template_name, {'form':form})

@login_required
@student_required
def results(request):
    template_name = 'home/AcadForm.html'
    form = ResultsForm()
    if request.method =='POST':
        form = ResultsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.batches = request.user.batch
            form.save()
            return redirect('home:home')
        else:
            form = ResultsForm()
    return render(request, template_name, {'form':form})

@login_required
@cr_required
def ScheDel(request, id):
    post = Schedule.objects.get(pk=id)
    post.delete()
    return redirect('home:home')

@login_required
@cr_required
def ReDel(request, id):
    post = Results.objects.get(pk=id)
    post.delete()
    return redirect('home:home')

@login_required
@cr_required
def AttDel(request, id):
    post = Attendance.objects.get(pk=id)
    post.delete()
    return redirect('home:home')

@login_required
@cr_required
def CampDel(request, id):
    post = CampusNews.objects.get(pk=id)
    post.delete()
    return redirect('home:home')

@login_required
@cr_required
def NacaDel(request, id):
    post = NonAcademic.objects.get(pk=id)
    post.delete()
    return redirect('home:home')


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
            return redirect('home:home')
        else:
            schedules = Schedule.objects.filter(heading__icontains = query)
            attendance = Attendance.objects.filter(heading__icontains = query)
            results = Results.objects.filter(heading__icontains = query)
            NAcadResults = NonAcademic.objects.filter(heading__icontains = query)
            CampResults =  CampusNews.objects.filter(heading__icontains = query)
            a = subject.objects.search(query)
            b = Ebook.objects.search(query)
            c = Paper.objects.search(query)
            d = Lecture.objects.search(query)
            ClubsResults = Clubs.objects.filter(heading__icontains = query)
            DetailsResults = Categories.objects.filter(heading__icontains = query)
            EventsResults = Events.objects.filter(heading__icontains = query)
            final = list(chain(schedules,attendance,results, NAcadResults, CampResults,a,b,c,d,ClubsResults ))
            length = len(final)+len(DetailsResults)+len(EventsResults)
            context = {'final':final, 'length':length,'EventsResults':EventsResults, 'DetailsResults':DetailsResults}
            return render(request, template_name, context)
