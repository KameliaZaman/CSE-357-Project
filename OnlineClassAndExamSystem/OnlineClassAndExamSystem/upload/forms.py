from django import forms
from .models import questionAndSolution
class questionAndSolutionForm(forms.ModelForm):
    """
    A class that inherits ModelForm class. Make a form for corresponding model class.
    """

    class Meta:
        model = questionAndSolution
        fields= ('subject','semester','question','solution')