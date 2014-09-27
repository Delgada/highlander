from registration.forms import RegistrationForm
from django import forms
 
class UserProfileForm(RegistrationForm):
    bio = forms.CharField(max_length = 5000, required = False )
    url = forms.URLField( required = False )
    location = forms.CharField( max_length = 2, required = False )
    first_name = forms.CharField( max_length = 10, required = False )
    last_name = forms.CharField( max_length = 10, required = False )

from core.models import UserProfile

class UserProfileEditForm( forms.ModelForm ):
    
    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False

    class Meta:
        model = UserProfile
        exclude = ("user",)