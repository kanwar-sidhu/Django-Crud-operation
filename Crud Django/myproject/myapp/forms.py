# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import person
 
# create a ModelForm
class personForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = person
        fields = "__all__"