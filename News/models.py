from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(blank=True)
    author = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    short_text = models.TextField()
    source_link = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.title
