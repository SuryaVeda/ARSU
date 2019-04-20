from django.shortcuts import render, redirect
from .models import subject, sideHeading
from .forms import subjectForm, sideHeadingForm
from itertools import chain
from django.contrib.auth.decorators import login_required
from home.decorators import student_required
# Create your views here.
@login_required
@student_required
def notes(request):
    template_name = 'notes/classNotes.html'
    subjects = subject.objects.order_by('pk')
    posts = sideHeading.objects.order_by('pk')
    return render(request, template_name, {'subjects':subjects, 'posts':posts})
@login_required
@student_required
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
def posts(request):
    template_name = 'notes/postForm.html'
    form = sideHeadingForm()
    if request.method =='POST':
       form = sideHeadingForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('notes:notes')
    else:
        form = sideHeadingForm()
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
            subjectResults = subject.objects.filter(heading__icontains = query)
            sideHeadingResults = sideHeading.objects.filter(heading__icontains = query)
            Results = list(chain(subjectResults,sideHeadingResults))
            context = {'Results':Results}
            return render(request, template_name, context)

    else:
        return render(request, template_name)
