from django.db import models

# Create your models here.

class Article(models.Model):
    CATEGORY = (
        ('politics', 'politics'),
        ('science', 'science'),
        ('tech', 'tech'),
    )
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now_add=True)
    article_category = models.CharField(max_length=10,choices=CATEGORY)
    content=models.TextField()
    source_link=models.TextField(max_length=2000)