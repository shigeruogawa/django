from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import TransactionTestCase
from accounts.models import User
from testing.models import Snippet
from django.template import Template, Context

import factory
from factory import fuzzy
import string
import datetime
from unittest import mock
import pytz
from django.utils import timezone
from testing.services import SnippetService

UserModel = get_user_model()


# class SnippetManagerTests(TestCase):
#     def test_public_snippet_manager(self):
#         user = get_user_model().objects.create_user(
#             username="c-data", email="ogawa@example", password="password"
#         )

#         TestingSnippet.objects.create(title="title1", is_draft=False)
#         TestingSnippet.objects.create(title="title2", is_draft=True)
#         # TestingSnippet.objects.create(title="title1", created_by=user, is_draft=False)
#         # TestingSnippet.objects.create(title="title2", created_by=user, is_draft=True)

#         snippets = TestingSnippet.public_objects.all()
#         self.assertEqual(len(snippets), 1)
#         self.assertEqual(snippets[0].title, "title1")


# class SnippetFormTests(TestCase):
#     def test_valid_when_given_long_title(self):
#         params = {
#             "title": "1234567890",
#             "code": print("Hello World"),
#             "description": "これは説明文です。",
#         }

#         snippet = TestingSnippet()
#         form = SnippetForm(params, instance=snippet)

#         self.assertTrue(form.is_valid())

#     def test_invalid_when_given_too_short_title(self):
#         params = {
#             "title": "123456789",
#             "code": print("echo hoge"),
#             "description": "これは説明文です。",
#         }

#         snippet = TestingSnippet()
#         form = SnippetForm(params, instance=snippet)
#         self.assertFalse(form.is_valid())

#     def test_mormalize_unicode_data(self):
#         params = {
#             "title": "ｱｲｳｴｵｱｲｳｴｵｱｲｳｴｵｱｲｳｴｵ",
#             "code": 'print("hoge")',
#             "description": "これは説明文です。",
#         }

#         snippet = TestingSnippet()
#         form = SnippetForm(params, instance=snippet)
#         form.is_valid()

#         actual = form.cleaned_data["title"]
#         # expected = 'abc'
#         expected = "アイウエオアイウエオアイウエオアイウエオ"
#         self.assertEqual(expected, actual)


# class SnippetCreateViewTests(TestCase):
    # def setUp(self):
    #     self.factory = RequestFactory()
    #     self.user = UserModel.objects.create_user(
    #         username="ogawa", email="ogawa@example", password="password"
    #     )

    # def test_should_return_200_if_sending_get_request(self):
    #     request = self.factory.get("/endpoint/of/create_snippet")
    #     request.user = self.user
    #     response = new_snippet(request)
    #     self.assertEqual(response.status_code, 200)

    # def test_should_return_302_if_not_authenticated(self):
    #     request = self.factory.get("/endpoint/of/create_snippet")
    #     request.user = AnonymousUser()
    #     response = new_snippet(request)
    #     self.assertIsInstance(response, HttpResponseRedirect)

    # def test_should_return_400_if_sending_empty_post(self):
    #     request = self.factory.post("/endpoint/of/create_snippet")
    #     request.user = self.user
    #     response = new_snippet(request)
    #     self.assertEqual(response.status_code, 400)

    # def test_should_return_200_if_sending_valid_post(self):
    #     request = self.factory.post(
    #         "/endpoint/of/create_snippet",
    #         data={
    #             "title": "メソッド呼び出し001",
    #             "code": "$this->target()",
    #             "description": "これは説明文です。",
    #         },
    #     )

    #     request.user = self.user
    #     response = new_snippet(request)
    #     self.assertEqual(response.status_code, 201)


class TestWcswidthFilter(TestCase):
    def test_single_width_letter(self):
        template = Template("{% load wcwidth_tags %}{{ message | wcwidth}}")
        context = Context({"message": "msg"})

        actual = template.render(context)
        self.assertEqual(actual, "3")

    def test_double_width_letter(self):
        template = Template("{% load wcwidth_tags %}{{ message | wcwidth}}")
        context = Context({"message": "あいうえお"})

        actual = template.render(context)
        self.assertEqual(actual, "10")


class UserModelTests(TransactionTestCase):
    fixtures = ["active_user"]

    def test_lookup_admin_user(self):
        admin = User.objects.filter(is_superuser=True)
        self.assertEqual(len(admin), 1)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = fuzzy.FuzzyText(length=5, chars=string.ascii_lowercase + "0123456789-")
    email = factory.Faker("email", locale="ja_JP")
    is_superuser = True


class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet

    title = fuzzy.FuzzyText(prefix="title_", length=16)
    code = fuzzy.FuzzyText(prefix="code_")
    # created_by = factory.SubFactory(UserFactory)
    description = fuzzy.FuzzyText(prefix="setusmei_", length=64)


current_datetime = datetime.datetime(
    year=2023, month=7, day=27, hour=0, tzinfo=pytz.timezone("Asia/Tokyo")
)


class LatestSnippetsTests(TestCase):
    @mock.patch("testing.services.timezone")
    def test_should_match_only_updated_two_days_ago(self, mock_timezone):
        mock_timezone.now.return_value = current_datetime
        mock_timezone.timedelta = timezone.timedelta
        
        print(f"日時:{current_datetime}")

        SnippetFactory(
            title="two", created_at=current_datetime - datetime.timedelta(days=2)
        )
        SnippetFactory(
            title="four", created_at=current_datetime - datetime.timedelta(days=4)
        )
        actual = SnippetService.latest_snippets(days=3, hour=0, minuts=0)
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].title, "two")
        
        for e in actual:
            print(f"結果日時:{e.created_at}")
