from django import forms
from django.core.exceptions import ValidationError
from .models import Snippet
import unicodedata


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')

    def clean_title(self):
        title = self.cleaned_data['title']
        title = unicodedata.normalize("NFKC", title)
        if len(title) < 10:
            raise ValidationError("タイトルの長さは10桁以上です。")
        return title
