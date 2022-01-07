from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import userAccount, discussionRoom

class myUserCreationForm(UserCreationForm):
    class Meta:
        model = userAccount
        fields = '__all__'

class roomForm(ModelForm):
    class Meta:
        model = discussionRoom
        fields = '__all__'
        exclude = ['hostName', 'roomParticipants']
    
class userForm(ModelForm):
    class Meta:
        model = userAccount
        fields ='__all__'