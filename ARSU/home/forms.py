from django import forms
from django.forms import ModelForm
from .models import Academic, NonAcademic, HospitalNews, CampusNews

class AcademicForm(ModelForm):
    #image = forms.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    class Meta:
        model = Academic
        fields = ['batches',  'heading','pdf', 'image', 'text']

class NAcademicForm(ModelForm):
    class Meta:
        model = NonAcademic
        fields = ['pdf', 'image', 'heading', 'text']

class HospitalNewsForm(ModelForm):
    class Meta:
        model = HospitalNews
        fields = ['pdf', 'image', 'heading', 'file', 'summary', 'url']
class CampusNewsForm(ModelForm):
    class Meta:
        model = CampusNews
        fields = ['pdf', 'image', 'heading', 'file', 'summary']
