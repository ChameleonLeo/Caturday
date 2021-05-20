from django import forms
from .models import CatPost


class CatPostForm(forms.ModelForm):

    class Meta:
        model = CatPost
        fields = ['catitle', 'catext']
