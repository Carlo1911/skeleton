from django.contrib import admin

from article.models import Article, Reporter


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'article_id',
        'article_heading',
        'article_body',
    )