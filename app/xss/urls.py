from django.urls import path

from xss import apps

urlpatterns = [path("target", apps.xss_view, name="xss_enter")]
