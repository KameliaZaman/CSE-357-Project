from .models import Video
from django.forms import ModelForm
from django import forms

class videoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=("caption","courseName","teacherId","video")
        # widgets = {
        #     'caption' : forms.CharField(attrs={'class':'form-control'}),
        #     'courseName' : forms.CharField(attrs={'class':'form-control'}),
        #     'teacherId' : forms.IntegerField(attrs={'class':'form-control'}),
        #     'video' : forms.FileField(attrs={'class':'form-control'})


        # }
        caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        courseName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        teacherId = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        video = forms.FileField(widget=forms.TextInput(attrs={'class': 'form-control'}))

      