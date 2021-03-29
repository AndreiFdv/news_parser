import requests
from bs4 import BeautifulSoup as bs
from django.core.management.base import BaseCommand
from newspaper import Article as NewsArticle

from News.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://www.reuters.com/world'
        html = requests.get(url)
        soup = bs(html.content, 'html.parser')

        body = soup.find(class_="column1 col col-10")

        links = body.find_all('a')

        reuters = 'https://www.reuters.com'

        urls = list()
        for link in links[:-1:]:
            urls.append(reuters + link['href'])

        urls = list(dict.fromkeys(urls))

        for url in urls:
            article = NewsArticle(url)
            article.download()
            article.parse()

            a = Article(title=article.title, content=article.text, date=article.publish_date, author=article.authors,
                        source_link=url)
            a.save()
