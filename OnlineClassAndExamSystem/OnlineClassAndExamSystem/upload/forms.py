from django import forms
from .models import questionAndSolution
class questionAndSolutionForm(forms.ModelForm):
    class Meta:
        model = questionAndSolution
        fields= ('subject','semester','question','solution')