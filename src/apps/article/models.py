from django.db import models
from common.models import CommonModel


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Reporter(CommonModel):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Reportero'
        verbose_name_plural = 'Reporteros'
