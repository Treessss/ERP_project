from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

# 登录模块


def index(request):
    return render(request,'flatter/index.html')

# 登陆页面
def login(request):
    return render(request,'flatter/login.html')

# 登陆信息验证


# 注册页面


# 注册页面验证

