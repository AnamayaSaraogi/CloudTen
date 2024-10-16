from django import forms
from .models import *
from django.forms import ModelForm

class faq(forms.Form):
    ques=forms.CharField(label="Enter your question",max_length=200)
    
