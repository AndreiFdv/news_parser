from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(blank=True)
    author = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True, null=True)
    short_text = models.TextField(blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True)
    img = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title
