from django.shortcuts import render, redirect
from .models import Topic, Mcq, FlashCard, Fact
from notes.models import subject, Lecture, Ebook, Paper
from .forms import McqForm, TopicForm, FlashCardForm, FactForm
from itertools import chain
from django.contrib.auth.decorators import login_required
from home.decorators import student_required
# Create your views here.
@login_required
def subs(request):
    template_name = 'mcq/subs.html'
    subjects = subject.objects.order_by('pk')
    return render(request, template_name, {'subjects':subjects})
@login_required
def sub(request, id):
    template_name = 'mcq/hola.html'
    subjects = subject.objects.order_by('pk')
    sub = subject.objects.get(pk=id)
    topics = Topic.objects.filter(subject = sub)
    mcqs = Mcq.objects.filter(subject=sub)
    facts = Fact.objects.filter(subject=sub)
    cards = FlashCard.objects.filter(subject=sub)
    questions = list(chain( mcqs, facts, cards))
    context = {'questions':questions, 'subjects':subjects, 'sub':sub, 'topics':topics, 'mcqs':mcqs, 'facts':facts, 'cards':cards}
    return render(request, template_name, context)

@login_required
@student_required
def mcq(request, id, pk):
    template_name = 'accounts/table.html'
    form = McqForm()
    if request.method =='POST':
       form = McqForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.subject = subject.objects.get(pk = pk)
          form.topic = Topic.objects.get(pk=id)
          form.save()
          return redirect('mcq:sticky')
    else:
        form = McqForm()
        return render(request, template_name, {'form':form})

    context = {'form':form}
    return render(request, template_name, context)
@login_required
@student_required
def cards(request, id, pk):
    template_name = 'accounts/table.html'
    form = FlashCardForm()
    if request.method =='POST':
       form = FlashCardForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.subject = subject.objects.get(pk = pk)
          form.topic = Topic.objects.get(pk=id)
          form.save()
          return redirect('mcq:sticky')
    else:
        form = FlashCardForm()
        return render(request, template_name, {'form':form})

    context = {'form':form}
    return render(request, template_name, context)
@login_required
@student_required
def facts(request, id, pk):
    template_name = 'accounts/table.html'
    form = FactForm()
    if request.method =='POST':
       form = FactForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.subject = subject.objects.get(pk = pk)
          form.topic = Topic.objects.get(pk=id)
          form.save()
          return redirect('mcq:sticky')
    else:
        form = FactForm()
        return render(request, template_name, {'form':form})

    context = {'form':form}
    return render(request, template_name, context)
@login_required
@student_required
def topic(request, id):
    template_name = 'accounts/table.html'
    form = TopicForm()
    if request.method =='POST':
       form = TopicForm(request.POST, request.FILES)
       if form.is_valid():
          form = form.save(commit=False)
          form.user = request.user
          form.subject = subject.objects.get(pk=id)
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
            PostResults = Post.objects.filter(heading__icontains = query)
            mcqResults = Mcq.objects.filter(question__icontains = query)
            Results = list(chain(subjectResults,PostResults, mcqResults))
            context = {'Results':Results}
            return render(request, template_name, context)

    else:
        return render(request, template_name)
