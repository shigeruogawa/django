from django.urls import path

from ViewPractice import views

urlpatterns = [
    path("", views.multi,name="multi"),
    path("submit", views.multi,name="multi"),
]
