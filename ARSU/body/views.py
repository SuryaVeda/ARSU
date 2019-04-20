from django.shortcuts import render, redirect
from body.models import Student, Detail
from django.contrib.auth.decorators import login_required
from home.decorators import student_required
# Create your views here.
@login_required
@student_required
def body(request):
    template_name = 'body/body.html'
    posts = Student.objects.order_by('pk')
    return render(request, template_name, {'posts':posts})
@login_required
@student_required
def details(request):
    template_name= 'body/details.html'
    details = Detail.objects.order_by('pk')
    return render(request, template_name, {'details':details})
