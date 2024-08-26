from django.apps import AppConfig
from django.db import models
from django import forms

class FormappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formapp'


class Snippet(models.Model):
    title = models.CharField('title', max_length=128)
    code = models.TextField('kode', blank=True)
    description = models.TextField('desc', blank=True)
    
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title','kode','desc')
