from news.models import Article, Subscriber
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail


def send_mails(Article, Subscriber) -> None:
    articles = Article.objects.order_by('-date')[:5].values_list('title', 'id')
    subscribers = Subscriber.objects.all()

    emails = []
    for i in list(subscribers):
        emails.append(i.email_address)

    messages = []
    for i in articles:
        article_link = Article.objects.get(id=list(i)[1]).get_absolute_url()
        link = 'http://127.0.0.1:8000' + article_link
        i = list(i)[0]
        messages.append((i, i + '\n' + str(link), 'ddddnews111@gmail.com', emails))
    send_mass_mail(tuple(messages), fail_silently=False)


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mails(Article, Subscriber)
