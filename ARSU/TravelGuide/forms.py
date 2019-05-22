from django import forms
from .models import Travel, Images


class TravelForm(forms.ModelForm):
    itinerary = forms.CharField(required = False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    budget = forms.CharField(required = False,widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    experience = forms.CharField(required = False,widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model = Travel
        fields = ['heading','itinerary','budget','experience', 'image']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Images
        fields = ['image']
