from django import forms
from .models import *


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speciality'].empty_label = 'Врач не выбран'
        self.fields['gender'].empty_label = 'Гендер не выбран'

    class Meta:
        model = Users
        fields = ['name', 'email', 'phone', 'speciality', 'gender', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input__name'}),
            'email': forms.TextInput(attrs={'class': 'input__item'}),
            'phone': forms.TextInput(attrs={'class': 'input__item'}),
            'speciality': forms.Select(attrs={'class': 'slc__item'}),
            'gender': forms.Select(attrs={'class': 'slc__gender'}),
            'avatar': forms.FileInput(attrs={'class': 'avatar__item__2'}),



        }



