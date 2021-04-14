from django.contrib import admin

from News.models import Article, TelegramUser

admin.site.register(Article)
admin.site.register(TelegramUser)
