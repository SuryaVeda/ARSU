from django.shortcuts import render, redirect
from body.models import Student, Detail
from django.contrib.auth.decorators import login_required
from .forms import Stu
from home.decorators import student_required, cr_required
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
@login_required
@cr_required
def addStudent(request):
    template_name = 'accounts/table.html'
    form = Stu()
    if request.method == 'POST' :
        form = Stu(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("body:body")
        else:
            form = Stu()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@cr_required
def editForm(request, id):
    template_name = 'accounts/table.html'
    instance = Student.objects.get(id=id)
    form = Stu(instance=instance)
    if request.method == 'POST' :
        form = Stu(request.POST or None, instance=instance)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
                form.save()
                instance.image = form.image
                instance.save()
            else:
                form.save()

            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("body:body")
        else:
            form = Stu(instance=instance)
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
