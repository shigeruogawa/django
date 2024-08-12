from django.urls import path

from snippets import views

urlpatterns = [
    path("/view", views.snippet_new,name="snippet_new"),
]
