from django.contrib import admin
from news.models import Article, TelegramUser, TelegraphArticle, Subscriber

admin.site.register(Article)
admin.site.register(TelegramUser)
admin.site.register(TelegraphArticle)
admin.site.register(Subscriber)