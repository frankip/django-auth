from django.forms import Form
from django import forms

from authapp.models import Profile 

# class ProfileForms(forms.Model)
class ProfileForm(forms.Form):
    
    class Meta:
        model = Profile
        exclude = ("user",)
