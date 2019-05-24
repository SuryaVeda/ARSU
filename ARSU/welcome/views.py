from django.shortcuts import render
from .models import slider
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def welcome(request):
    template_name = 'welcome/welcome.html'
    slides = slider.objects.order_by('pk')
    return render(request, template_name, {'slides':slides, 'open':open})
