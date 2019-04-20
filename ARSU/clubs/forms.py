from .models import Events
from django.forms import ModelForm

class EventForms(ModelForm):
    class Meta:
        model = Events
        fields = ['post', 'month', 'date', 'heading', 'text', 'image']
