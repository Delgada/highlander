from registration.forms import RegistrationForm
from django import forms
 
class UserProfileForm(RegistrationForm):
    bio = forms.CharField(max_length = 5000, required = False )
    url = forms.URLField( required = False )
    location = forms.CharField( max_length = 2, required = False )
    first_name = forms.CharField( max_length = 10, required = False )
    last_name = forms.CharField( max_length = 10, required = False )

#from django import forms
#from .models import UserProfile

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        exclude = ["user"]