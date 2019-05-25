from django import forms
from django.forms import ModelForm
from .models import Schedule, Attendance, Results, NonAcademic, CampusNews

class ScheduleForm(ModelForm):
    #image = forms.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    class Meta:
        model = Schedule
        fields = ['heading','pdf', 'image', 'text']

class AttendanceForm(ModelForm):
    #image = forms.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    class Meta:
        model = Attendance
        fields = ['heading','pdf', 'image', 'text', 'link']
class ResultsForm(ModelForm):
    #image = forms.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    class Meta:
        model = Results
        fields = ['heading','pdf', 'image', 'text']


class NAcademicForm(ModelForm):
    class Meta:
        model = NonAcademic
        fields = ['pdf', 'image', 'heading', 'text']

class CampusNewsForm(ModelForm):
    class Meta:
        model = CampusNews
        fields = ['pdf', 'image', 'heading', 'file', 'summary']
