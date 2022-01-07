from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import userAccount, discussionRoom

class myUserCreationForm(UserCreationForm):
    """ This is the user account creation form inherited from UserCreationForm.

    Class:
    -----
    'Model' field shows which Model your Form would be created from and 
    'Fields' field shows which fields from the Model class to show in your new Form.
    """
    class Meta:
        model = userAccount
        fields = '__all__'

class roomForm(ModelForm):
    """ This is the room creation form inherited from ModelForm.

    Class:
    -----
    'Model' field shows which Model your Form would be created from and 
    'Fields' field shows which fields from the Model class to show in your new Form.
    The exclude attribute tells Django what fields from the model not to include in the form.

    """
    class Meta:
        model = discussionRoom
        fields = '__all__'
        exclude = ['hostName', 'roomParticipants']
    
class userForm(ModelForm):
    """ This is the user form inherited from ModelForm.

    Class:
    -----
    'Model' field shows which Model your Form would be created from and 
    'Fields' field shows which fields from the Model class to show in your new Form.
    """
    class Meta:
        model = userAccount
        fields ='__all__'
