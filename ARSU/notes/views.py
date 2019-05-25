from django.shortcuts import render, redirect
from .models import subject, Ebook, Paper, Lecture
from .forms import subjectForm, EbookForm, PaperForm, LectureForm
from itertools import chain
from django.contrib.auth.decorators import login_required
from home.decorators import student_required, cr_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
@student_required
def subs(request):
    template_name = 'notes/subjects.html'
    subjects = subject.objects.order_by('pk')
    return render(request, template_name, {'subjects':subjects})
@login_required
def notes(request, id):
    template_name = 'notes/classNotes.html'
    sub = subject.objects.get(pk=id)
    Eposts = Ebook.objects.filter(post=sub)
    Pposts = Paper.objects.filter(post=sub)
    Lposts = Lecture.objects.filter(post=sub)
    return render(request, template_name, {'sub':sub, 'Eposts':Eposts, 'Lposts':Lposts, 'Pposts':Pposts})

@login_required
@cr_required
def subject_form(request):
    template_name = 'notes/subjectForm.html'
    form = subjectForm()
    if request.method =='POST':
       form = subjectForm(request.POST)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('notes:notes')
    else:
        form = subjectForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def Pposts(request,id):
    template_name = 'notes/postForm.html'
    form = PaperForm()
    if request.method =='POST':
       form = PaperForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.post = subject.objects.get(pk=id)
          form.save()
          return redirect('notes:notes')
    else:
        form = PaperForm()
        return render(request, template_name, {'form':form})

@login_required
@student_required
def Lposts(request, id):
    template_name = 'notes/postForm.html'
    form = LectureForm()
    if request.method =='POST':
       form = LectureForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.post = subject.objects.get(pk=id)
          form.save()
          return redirect('notes:notes')
    else:
        form = LectureForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def Eposts(request, id):
    template_name = 'notes/postForm.html'
    form = EbookForm()
    if request.method =='POST':
       form = EbookForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.post = subject.objects.get(pk=id)
          form.save()
          return redirect('notes:notes')
    else:
        form = EbookForm()
        return render(request, template_name, {'form':form})
@login_required
@student_required
def search(request):
    template_name = 'home/search.html'
    if request.method == 'GET':
        query = request.GET.get('q')
        submitButton = request.GET.get('submit')
        if query == "":
            return redirect('notes:notes')
        else:
            a = subject.objects.search(query)
            b = Ebook.objects.search(query)
            c = Paper.objects.search(query)
            d = Lecture.objects.search(query)
            final = list(chain(a, b, c, d))
            length = len(results)
            return render(request, template_name, {'final':final, 'length':length})
    else:
        return redirect('notes:notes')
