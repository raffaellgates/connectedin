from django import forms

from django.forms import ModelForm
from timeline.models import Publicacao

class PublicarForm(ModelForm):
    class Meta:
        model = Publicacao
        fields = ['publicacao']