# coding:utf-8
from django.urls import path, re_path
from website.views import Home, HomeCache

urlpatterns = [
    re_path(r'^$', Home.as_view(), name='home'),
    re_path(r'cache/', HomeCache.as_view(), name='cache'),
]
