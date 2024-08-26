# from django.db import models

# Create your models here.
from django.apps import AppConfig
from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class FormappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "formapp"


# class Formapp(models.Model):
#     title = models.CharField("title", max_length=128)
#     code = models.TextField("kode", blank=True)
#     description = models.TextField("desc", blank=True)


# class FormappForm(forms.ModelForm):
#     class Meta:
#         model = Formapp
#         fields = ("title", "code", "description")


# def tel_validator(value):
#     if not value.isdigit():
#         raise ValidationError(
#             _("detect non digit character: %{value}"),
#             code="invalid",
#             params={"value": value},
#         )


# class Person(models.Model):
#     tel = models.CharField(max_length=12, validators=[tel_validator])


class IntegerField(forms.Field):
    def to_python(self, value):
        try:
            i = int(value)
        except (ValidationError, TypeError):
            raise ValidationError("不正なデータです", code="invalid")
        return i

    def validate(self, value):
        return super().validate(value)


    def custom_validator(value):
class FooForm(forms.Form):
    age = IntegerField(validators=[custom_validator])

    def clean_age(self):
        value = self.cleaned_data["age"]

        return value

    def clean(self):
        data = self.serialized_data

        return data
