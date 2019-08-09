from django.db import models

class Article(models.Model):
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Reporter(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Reportero'
        verbose_name_plural = 'Reporteros'
