from django.db import models

# Create your models here.

class article(models.Model):
    CATEGORY = (
        ('politics', 'politics'),
        ('science', 'science'),
        ('tech', 'tech'),
    )
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now_add=True)
    article_category = models.CharField(max_length=10,choices=CATEGORY,null=True)
    content=models.TextField()
    source_link=models.TextField(max_length=2000,blank=True)