from django.contrib import admin

from news.models import Article, TelegramUser

admin.site.register(Article)
admin.site.register(TelegramUser)
