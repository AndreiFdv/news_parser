import os

from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from news.models import Article, Subscriber


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = Article.objects.all().order_by('-date')[:5]
        subscribers = Subscriber.objects.all()

        emails = [x.email_address for x in subscribers]

        msg = ""
        for article in articles:
            link = f'http://127.0.0.1:8000{article.get_absolute_url()}'
            msg += f'{article.title}: {link}\n'

        send_mail("Subscription", msg, os.getenv('MSG_EMAIL'), emails)
