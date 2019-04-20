from django.shortcuts import render, redirect
from .forms import VisitorRegisterForm, StudentRegisterForm, CrRegisterForm

# Create your views here.
def login(request):
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
            user = form.save()
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
            user = form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("/accounts/login")
        else:
            form = CrRegisterForm()
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
