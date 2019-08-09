# coding:utf-8
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

import views

urlpatterns = [
    path(
        r'^validate/?$',
        csrf_exempt(views.SABMillerUserValidation.as_view()),
        name='validate'
    ),
    path(
        r'^register/?$',
        csrf_exempt(views.SABMillerUserRegister.as_view()),
        name='register'
    ),
]
