from django import forms
from django.forms import ModelForm
from project.models import MyModel




class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = [
            'y_n', 
            'providers'
        ]


        


