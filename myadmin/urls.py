"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # 登陆模块
    path('',LoginViews.index,name="All_index"),
    path('login/',LoginViews.login,name="Login_index"),
    path('dologin/',LoginViews.dologin,name="Login_dologin"),
    path('yzm/',LoginViews.check_code,name="Login_check_code"),

    # 注册模块
    path('register/',LoginViews.register,name="Login_register"),
    path('doregister/', LoginViews.doregister, name="Login_doregister"),

]
