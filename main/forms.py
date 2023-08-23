from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, FollowUp

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class PostTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields=["title", "description","department"]
        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':25}),
        }  
           
class PostFollowup(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields=["description"]
        widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':15}),
        }    
