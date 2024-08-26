from django.apps import AppConfig
from django.contrib.auth.decorates import login_required

class CsrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'csrf'
