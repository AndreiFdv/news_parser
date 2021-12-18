import logging
import os

from django.core.management.base import BaseCommand
from telegram import Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (CallbackContext, CommandHandler, ConversationHandler,
                          Filters, MessageHandler, Updater)

from news.models import Article, TelegramUser

UNSUBSCRIBE, ECHO = range(2)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def send_message(article: Article) -> None:
    users = TelegramUser.objects.only("user_id")
    bot = Bot(token=os.getenv('TELEGRAM_BOT'))
    link = 'http://127.0.0.1:8000' + article.get_absolute_url()

    for user in users:
        message = f'<b>{article.title}</b>\n{article.short_text} \n<a href="{link}">Read more</a>'

        bot.send_message(chat_id=user.user_id, text=message, parse_mode='HTML')


def send_telegraph_msg(link: str) -> None:
    users = TelegramUser.objects.only("user_id")
    bot = Bot(token=os.getenv('TELEGRAM_BOT'))

    for user in users:
        bot.send_message(chat_id=user.user_id, text=link)


def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name

    obj, created = TelegramUser.objects.get_or_create(
        user_id=user_id,
        user_name=user_name
    )

    reply_keyboard = [['Unsubscribe', 'Help', 'Other']]

    if created:
        logger.info(f'{user_id}:{user_name} subscribed')
        update.message.reply_text(
            f'{user_name}, you have been successfully subscribed\n'
            'Send /unsubscribe to stop talking to me.\n\n',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, resize_keyboard=True
            ),
        )


def unsubscribe(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id

    TelegramUser.objects.filter(user_id=user_id).delete()

    logger.info(f'Message: {update.message.text} from: {user.first_name}')
    update.message.reply_text(
        f'{user.first_name}, you have been successfully unsubscribed',
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info(f'User {user.id} send a message: {update.message.text}')
    update.message.reply_text(update.message.text)


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(os.getenv('TELEGRAM_BOT'))

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(MessageHandler(Filters.regex('^unsubscribe'), unsubscribe))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
