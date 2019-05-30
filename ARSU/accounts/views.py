from django.shortcuts import render, redirect, get_object_or_404
from .forms import VisitorRegisterForm, StudentRegisterForm, CrRegisterForm,ProfileForm, TableForm,ActivitesForm, RemainderForm
from .models import Profile, Remainders, Activites, Timetable, User
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from home.decorators import student_required, cr_required
# Create your views here.
def signin(request):
    template_name = 'registration/login.html'
    return render(request, template_name)

def visitor(request):
    template_name = 'accounts/signup.html'
    form = VisitorRegisterForm()
    if request.method == 'POST' :
        form = VisitorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("/accounts/login")
        else:
            form = VisitorRegisterForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})

def student(request):
    template_name = 'accounts/signup.html'
    form = StudentRegisterForm()
    if request.method == 'POST' :
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            instance = form.save()
            Profile.objects.create(email = instance.email, name= instance.username)
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("/accounts/login")
        else:
            form = StudentRegisterForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
def cr(request):
    template_name = 'accounts/signup.html'
    form = CrRegisterForm()
    if request.method == 'POST' :
        form = CrRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save()
            user = User.objects.get(email = instance.email)
            Profile.objects.create(email = instance.email, name= instance.username, user =user)
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("/accounts/login")
        else:
            form = CrRegisterForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@student_required
def profile(request):
    template_name = 'accounts/profile.html'
    profile = Profile.objects.get(email = request.user.email)
    remainders =Remainders.objects.filter(user = request.user)
    timetables = Timetable.objects.filter(user = request.user)
    activities = Activites.objects.filter(user=request.user)
    table = Activites.objects.filter(date = date.today(), user=request.user)
    context = {'profile':profile, 'remainders':remainders,'timetables':timetables, 'activities':activities, "table":table}
    return render(request, template_name, context)
@login_required
@student_required
def profileForm(request, id):
    template_name = 'accounts/table.html'
    instance = Profile.objects.get(id=id)
    form = ProfileForm(instance=instance)
    if request.method == 'POST' :
        form = ProfileForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("accounts:profile")
        else:
            form = ProfileForm(instance=instance)
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@student_required
def table(request):
    template_name = 'accounts/table.html'
    form = TableForm()
    if request.method == 'POST' :
        form = TableForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("accounts:profile")
        else:
            form = TableForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@student_required
def activities(request, id):
    template_name = 'accounts/table.html'
    form = ActivitesForm()
    if request.method == 'POST' :
        form = ActivitesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.table = Timetable.objects.get(pk=id)
            instance.user = request.user
            form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("accounts:profile")
        else:
            form = ActivitesForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@student_required
def remainders(request):
    template_name = 'accounts/table.html'
    form = RemainderForm()
    if request.method == 'POST' :
        form = RemainderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("accounts:profile")
        else:
            form = RemainderForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
@login_required
@student_required
def Rdel(request, obj_id):
    remainder = Remainders.objects.filter(user = request.user, pk = obj_id)
    remainder.delete()
    return redirect('accounts:profile')
@login_required
@student_required
def Tdel(request, obj_id):
    table = Timetable.objects.filter(user = request.user, pk = obj_id)
    table.delete()
    return redirect('accounts:profile')
@login_required
@student_required
def Adel(request, obj_id):
    post = Activites.objects.filter(user = request.user, pk = obj_id)
    post.delete()
    return redirect('accounts:profile')
