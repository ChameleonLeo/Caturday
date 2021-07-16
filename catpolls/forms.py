from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Catuestion, Cachoice


class CatuestionForm(forms.ModelForm):

    class Meta:
        model = Catuestion
        fields = ['catuestion_text', 'catuestion_image']
        labels = {'catuestion_text': _('Question'),
                  'catuestion_image': _('Image')}


class CahoiceForm(forms.ModelForm):

    class Meta:
        model = Cachoice
        extra = 3
        fields = ['cachoice_text']
        labels = {'cachoice_text': _('answer')}
        widgets = {
            'choice': forms.TextInput(attrs={'type': 'hidden',
                                             'id': 'payload',
                                             'class': 'form-control',
                                             'required': True})}


PollChoiceFormSet = forms.modelformset_factory(Cachoice,
                                               form=CahoiceForm,
                                               extra=2,
                                               can_delete=False)
