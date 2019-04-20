from django import forms
from notes.models import subject, sideHeading

class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ['heading']

class sideHeadingForm(forms.ModelForm):
    class Meta:
        model = sideHeading
        fields = ['post','ebooks_pdf','lectures_pdf','papers_pdf', 'image', 'heading']
