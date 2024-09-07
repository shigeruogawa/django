from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("コード", max_length=255)
    email = models.CharField("説明", max_length=255)
    password = models.CharField("パスワード", max_length=32)
    is_superuser = models.BooleanField("管理者か")

    class Meta:
        db_table = "users"
