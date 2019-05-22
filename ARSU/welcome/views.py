from django.shortcuts import render
from .models import slider
# Create your views here.
def welcome(request):
    template_name = 'welcome/welcome.html'
    slides = slider.objects.order_by('pk')
    return render(request, template_name, {'slides':slides, 'open':open})
