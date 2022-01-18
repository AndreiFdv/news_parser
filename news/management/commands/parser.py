import os

from django.core.management.base import BaseCommand
from newsplease import NewsPlease
from telegraph import Telegraph

from news.management.commands import bot
from news.models import Article, TelegraphArticle
from news.news_sites import RSSNews

RSS_Links = [
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'http://feeds.foxnews.com/foxnews/world',
    'https://www.buzzfeed.com/world.xml',
    'https://www.aljazeera.com/xml/rss/all.xml',
]


class Command(BaseCommand):
    def handle(self, *args, **options):

        news = RSSNews(RSS_Links)
        telegraph = Telegraph(access_token=os.getenv('TELEGRAPH_ACCESS_TOKEN'))

        if news.urls:
            for url, date in news.urls.items():
                article = NewsPlease.from_url(url)

                a = Article(
                    author=', '.join(article.authors) or 'Anonymous',
                    title=article.title,
                    short_text=article.description,
                    content=article.maintext,
                    date=date,
                    source_link=url,
                    img=article.image_url
                )
                a.save()

                response = telegraph.create_page(
                    title=a.title,
                    html_content=a.content
                )

                TelegraphArticle(
                    title=a.title,
                    link=response['url']
                ).save()

                bot.send_telegraph_msg(response['url'])

        self.stdout.write(self.style.SUCCESS('Success'))
