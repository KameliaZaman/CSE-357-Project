from .models import Video
from django.forms import ModelForm
from django import forms

class videoForm(forms.ModelForm):
    """
    This is the form to upload class recording.

    Class:
    -----
    'Model' field shows which Model your Form would be created from.
    'fields' field shows which fields from the Model class to show in your form.    
    """
    class Meta:
        model=Video
        fields=("caption","courseName","teacherId","video")

      