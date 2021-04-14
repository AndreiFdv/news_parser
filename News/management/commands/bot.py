import os

from django.core.management.base import BaseCommand
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

from News.models import TelegramUser, Article


def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name

    t = TelegramUser(user_id=user_id, user_name=user_name)
    t.save()


def send_message(article: Article) -> None:
    users = TelegramUser.objects.all()
    bot = Bot(token=os.getenv('TELEGRAM_BOT'))
    link = 'http://127.0.0.1:8000' + article.get_absolute_url()

    for user in users:
        message = f'<b>{article.title}</b>\n{article.short_text} \n<a href="{link}">Read more</a>'

        bot.send_message(chat_id=user.user_id, text=message, parse_mode='HTML')


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(os.getenv('TELEGRAM_BOT'))

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))

        updater.start_polling()
        updater.idle()
