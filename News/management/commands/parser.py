from django.core.management.base import BaseCommand
from newspaper import Article as NewsArticle

from News.models import Article
from News.news_sites import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        reuters = Reuters('https://www.reuters.com/world')

        nyt = RSSNews('https://rss.nytimes.com/services/xml/rss/nyt/World.xml')
        fox = RSSNews('http://feeds.foxnews.com/foxnews/world')

        c_dict = {**nyt.urls, **fox.urls}

        if reuters.urls:
            for url in reuters.urls:
                article = NewsArticle(url)
                article.download()
                article.parse()

                a = Article(title=article.title,
                            short_text=article.meta_description,
                            content=article.text,
                            date=article.publish_date,
                            author=article.authors,
                            source_link=url)
                a.save()

        if c_dict:
            for url, date in c_dict.items():
                article = NewsArticle(url)
                article.download()
                article.parse()

                a = Article(title=article.title,
                            short_text=article.meta_description,
                            content=article.text,
                            date=date,
                            author=article.authors,
                            source_link=url)
                a.save()
