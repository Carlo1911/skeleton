# coding:utf-8
from django.views.generic import TemplateView
from django.core.cache import cache
from django.shortcuts import render

from website.tasks import print_name_celery

class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        cache.set('my_key', 'hello, world!', 30)
        test = cache.get('my_key')
        print(test)
        return render(request, self.template_name)

class HomeCache(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        test = cache.get('my_key')
        print(test)
        print_name_celery.delay('Carlo')
        return render(request, self.template_name)