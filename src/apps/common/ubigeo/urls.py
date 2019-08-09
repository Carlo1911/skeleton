# coding:utf-8
from django.urls import path

import views

urlpatterns = [
    path(r'^$', views.UbigeoView.as_view(), name='ubigeo'),
]
