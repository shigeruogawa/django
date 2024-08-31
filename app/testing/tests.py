from django.contrib.auth import get_user_model
from django.test import TestCase
from testing.models import Snippet
from testing.form import SnippetForm


class SnippetManagerTests(TestCase):
    def test_public_snippet_manager(self):
        user = get_user_model().objects.create_user(
            username="c-data", email="ogawa@example", password="password"
        )

        Snippet.objects.create(title="title1", created_by=user, is_draft=False)
        Snippet.objects.create(title="title2", created_by=user, is_draft=True)

        snippets = Snippet.public_objects.all()
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].title, "title1")


class SnippetFormTests(TestCase):
    def test_valid_when_given_long_title(self):
        params = {
            "title": "1234567890",
            "code": print("Hello World"),
            "description": "これは説明文です。",
        }

        snippet = Snippet()
        form = SnippetForm(params, instance=snippet)

        self.assertTrue(form.is_valid())

    def test_invalid_when_given_too_short_title(self):
        params = {
            "title": "123456789",
            "code": print("echo hoge"),
            "description": "これは説明文です。",
        }

        snippet = Snippet()
        form = SnippetForm(params, instance=snippet)
        self.assertFalse(form.is_valid())

    def test_mormalize_unicode_data(self):
        params = {
            'title': 'ｱｲｳｴｵｱｲｳｴｵｱｲｳｴｵｱｲｳｴｵ',
            'code': 'print("hoge")',
            'description': 'これは説明文です。'
        }
        
        snippet = Snippet()
        form = SnippetForm(params, instance=snippet)
        form.is_valid()
        
        actual = form.cleaned_data['title']
        # expected = 'abc'
        expected = 'アイウエオアイウエオアイウエオアイウエオ'
        self.assertEqual(expected, actual)
