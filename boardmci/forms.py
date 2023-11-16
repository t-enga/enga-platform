from django import forms
from .models import Mdp,Mci,Part
from django.forms.widgets import DateInput, TimeInput
from django.utils import timezone


class AddMci(forms.ModelForm):
    class Meta:
        model=Mci
        fields = '__all__'
        
class AddMdp(forms.ModelForm):
    class Meta:
        model=Mdp
        fields = '__all__'
        
class AddPart(forms.ModelForm):
    class Meta:
        model=Part
        fields = '__all__'