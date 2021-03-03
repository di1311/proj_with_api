from django import forms
from .models import Games
""" Форма, которая принимает название игры """


class statisticsForm(forms.ModelForm):
    class Meta:
        model = Games


