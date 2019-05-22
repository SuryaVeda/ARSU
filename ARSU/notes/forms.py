from django import forms
from notes.models import subject, Ebook, Lecture, Paper

class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ['heading']

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['pdf','image', 'heading', 'link']

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['pdf','image', 'heading', 'link']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['pdf','image', 'heading', 'link']
