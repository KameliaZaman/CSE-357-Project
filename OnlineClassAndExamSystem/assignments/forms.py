from django import forms
from django.db import models
from django.forms import fields
from .models import AssignmentsSubmit, AssignmentsUpload

  
class dateForm(forms.ModelForm):
    """
    This is the assignment creation form.

    Class:
    -----
    'Model' field shows which Model your Form would be created from.
    'fields' field shows which fields from the Model class to show in your form.    
    'widgets' fields use to apply some classes to beautify the form.
    """
    class Meta:
        model=AssignmentsUpload
        fields=("courseName","topicName","submissionDate","submissionTime","files") 
        widgets = {
         'courseName': forms.TextInput(attrs={'class':'form-control'}), 
         'topicName': forms.TextInput(attrs={'class':'form-control'}), 
         'submissionDate': forms.DateInput(attrs={'type':'date','class':'form-control'}),
         'submissionTime': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
         'files':forms.FileInput(attrs={'class':'form-control'}),

        }

class submissionForm(forms.ModelForm):
    """
    This is the assignment submission form.

    Class:
    -----
    'Model' field shows which Model your Form would be created from.
    'fields' field shows which fields from the Model class to show in your form.    
    'widgets' fields use to apply some classes to beautify the form.
    """
    class Meta:
        model=AssignmentsSubmit
        fields=("studentName","studentId","questionFile","answerFile") 
        widgets = {
         'studentName': forms.TextInput(attrs={'class':'form-control'}), 
         'studentId': forms.TextInput(attrs={'class':'form-control'}), 
         'questionFile': forms.FileInput(attrs={'class':'form-control'}),
         'answerFile': forms.FileInput(attrs={'class':'form-control'}),
        
        }

   
