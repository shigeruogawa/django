from django.apps import AppConfig
from django.db import models
from django import forms

class FormappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formapp'
