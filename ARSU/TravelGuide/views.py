from django.shortcuts import render, redirect, get_object_or_404
from .forms import TravelForm, ImageForm
from .models import Travel,Images
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from home.decorators import student_required

# Create your views here.
@login_required
def travel(request):
    template_name = 'TravelGuide/travel.html'
    posts = Travel.objects.order_by('pk')
    images = Images.objects.all()
    context = {'images':images, 'posts':posts}
    return render(request, template_name, context)
@login_required
@student_required
def addTrip(request):
    template_name = 'TravelGuide/TravelForm.html'
    form = TravelForm()
    if request.method =='POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect('TravelGuide:travel')
        else:
            form = TravelForm()
    return render(request, template_name, {'form':form})
@login_required
@student_required
def addImages(request, id):
    template_name = 'home/AcadForm.html'
    if request.method =='POST':
       form = ImageForm(request.POST, request.FILES)
       post = Travel.objects.get(pk=id)
       if form.is_valid():
          if request.FILES:
             for f in request.FILES.getlist('image'):
                 Images.objects.create(post = post, image = f)

          return redirect('TravelGuide:travel')
    else:
        form = ImageForm()
        return render(request, template_name, {'form':form})

@login_required
@student_required
def editTrip(request, id):
    template_name = 'accounts/table.html'
    instance = Travel.objects.get(id=id)
    form = TravelForm(instance=instance)
    if request.method == 'POST' :
        form = TravelForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect("TravelGuide:travel")
        else:
            form = TravelForm(instance=instance)
            return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})
