from django import forms
from .models import DM


class DFo(forms.ModelForm):
    class Meta:
        model = DM
        fields = '__all__'
