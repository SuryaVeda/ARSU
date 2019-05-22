from django import forms
from .models import Student, Detail

class Stu(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['designation','name','batch','phone','email','image']
