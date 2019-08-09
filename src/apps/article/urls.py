# -*- coding: utf-8 -*-
from rest_framework import routers
from article.views import ArticleViewSet, ReporterViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'reporter', ReporterViewSet)
urlpatterns = router.urls
