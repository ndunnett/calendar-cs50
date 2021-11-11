from django import forms
from django.forms.widgets import TextInput

from . import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        widgets = {
            'background_colour': TextInput(attrs={'type': 'color'}),
            'text_colour': TextInput(attrs={'type': 'color'}),
        }
