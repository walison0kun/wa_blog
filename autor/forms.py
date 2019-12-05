from django import forms
from.import models

class CreateAuth(forms.ModelForm):
    class Meta:
        model = models.author
        fields = ['nome', 'idade']