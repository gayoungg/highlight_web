from django import forms
from .models import MusicStorage


class UploadForm(forms.ModelForm):
    class Meta:
        model = MusicStorage
        fields='__all__'