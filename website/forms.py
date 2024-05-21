from django import forms 
from django.forms import ModelForm
from .models import Subscribe



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'