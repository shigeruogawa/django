# from django.http import HttpRequest
# from django.test import TestCase
# from snippets.views import top

# class TopPageViewTest(TestCase):
#     def test_top_returns_200(self):
#         request = HttpRequest()
#         response = top(request)
#         self.assertEqual(response.status_code, 200)

#     def test_top_returns_expected_content(self):
#         request = HttpRequest()
#         response = top(request)
#         self.assertEqual(response.content, b"Hello  World")


from django.test import TestCase
# 初期ビューがテキストを返す

# class TopPageTests(TestCase):
#     def test_top_returns_200(self):
#         response = self.client.get("/")
#         self.assertEquals(response.status_code, 200)

#     def test_top_returns_expected_content(self):
#         response = self.client.get("/")
#         self.assertEquals(response.content, b"Hello   World")

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット",status_code = 200)
        
    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")
        
from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()

class TopPageRenderSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test",
            email = "test@example.com",
            password = "password"
        )
        
        self.snippet = Snippet.objects.create(
            title="title",
            code="print('hello')",
            description="description",
            created_by=self.user,
        )
    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)
        
    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)
        
class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="1@example.com",
            password="password"
        )
        
        self.snippet = Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
            created_by=self.user
        )
        
    def test_should_use_expected_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")
        self.assertContains(response, self.snippet.title, status_code=200)
        
    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippet/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)
        
class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "testing",
            email = "hoge@example.com",
            password = "secret"
    )
        self.client.force_login(self.user)
    
    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response, "登録",status_code=200)
        
    def test_create_snippet(self):
        data = {'title': 'タイトル','code' : 'echo ogawa','description':'解説'}
        self.client.post("/snippets/new",data)
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('解説',snippet.description)
        
