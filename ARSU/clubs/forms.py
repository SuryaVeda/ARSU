from .models import Events, Categories, Clubs
from django.forms import ModelForm
from django import forms
class EventForms(ModelForm):
    date = forms.DateField(input_formats=['%m/%d/%Y'], widget = forms.TextInput(attrs={
        'id': 'datepicker-5'}))
    time = forms.TimeField(input_formats=['%H:%M:%S %p'], widget = forms.TextInput(attrs={
        'id': 'timepicker-1'}))
    class Meta:
        model = Events
        fields = ['date','time', 'heading', 'text', 'image']
class ClubsForm(ModelForm):
    class Meta:
        model = Clubs
        fields = ['heading', 'text', 'image']
class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['heading', 'img']
