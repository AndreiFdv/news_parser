from django.contrib import admin

from news.models import Article, TelegramUser, TelegraphArticle

admin.site.register(Article)
admin.site.register(TelegramUser)
admin.site.register(TelegraphArticle)
