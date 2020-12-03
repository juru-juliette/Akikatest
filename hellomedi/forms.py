from django import forms

from .models import *
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=100)
    email = forms.EmailField(label='Email')

class PostForm (forms.ModelForm):
    class Meta:
         model = Appointment

         exclude = ['middle_name']