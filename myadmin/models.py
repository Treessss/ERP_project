from django.db import models

# Create your models here.

# 用户
class Users(models.Model):
    username = models.CharField(max_length=11)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=50,null=True)


