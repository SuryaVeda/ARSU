from django.shortcuts import render, redirect
from .models import Topic, Mcq
from notes.models import subject, sideHeading
from .forms import McqForm, TopicForm
from itertools import chain
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def subs(request):
    template_name = 'mcq/subs.html'
    subjects = subject.objects.order_by('pk')
    return render(request, template_name, {'subjects':subjects})
@login_required
def Anatomy (request):
    template_name = 'mcq/Anatomy.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Physiology (request):
    template_name = 'mcq/P.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Biochemistry (request):
    template_name = 'mcq/B.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Pathology(request):
    template_name = 'mcq/pat.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Pharmacology(request):
    template_name = 'mcq/pha.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Microbiology(request):
    template_name = 'mcq/M.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Forensic(request):
    template_name = 'mcq/F.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def optha(request):
    template_name = 'mcq/O.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def ENT(request):
    template_name = 'mcq/E.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Orthopaedics(request):
    template_name = 'mcq/ort.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def CFM(request):
    template_name = 'mcq/C.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Medicine(request):
    template_name = 'mcq/med.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Surgery(request):
    template_name = 'mcq/S.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def Pediatrics(request):
    template_name = 'mcq/ped.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def OBG(request):
    template_name = 'mcq/obg.html'
    topics = Topic.objects.order_by('pk')
    subjects = subject.objects.order_by('pk')
    mcqs = Mcq.objects.order_by('pk')
    context = {'topics':topics, 'mcqs':mcqs, 'subjects':subjects}
    return render(request, template_name, context)
@login_required
def addMcq(request):
    template_name = 'mcq/form.html'
    if request.method =='POST':
       form = McqForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('mcq:sticky')
    else:
        form = McqForm()
        return render(request, template_name, {'form':form})

    context = {'form':form}
    return render(request, template_name, context)
@login_required
def addTopic(request):
    template_name = 'mcq/Topicform.html'
    if request.method =='POST':
       form = TopicForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.save()
          return redirect('mcq:sticky')
    else:
        form = TopicForm()
        return render(request, template_name, {'form':form})

    context = {'form':form}
    return render(request, template_name, context)
@login_required
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
            mcqResults = Mcq.objects.filter(question__icontains = query)
            Results = list(chain(subjectResults,sideHeadingResults, mcqResults))
            context = {'Results':Results}
            return render(request, template_name, context)

    else:
        return render(request, template_name)
