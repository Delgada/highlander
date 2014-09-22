from registration.forms import RegistrationForm
from django import forms
 
class UserProfileForm(RegistrationForm):
    #intent to use django gis for location
    #location = 
    url = forms.URLField( required = False )