from django.core.management.base import BaseCommand

from newsplease import NewsPlease

from news.management.commands import bot
from news.models import Article
from news.news_sites import Reuters, RSSNews

RSS_Links = [
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'http://feeds.foxnews.com/foxnews/world',
    'https://www.buzzfeed.com/world.xml',
    'https://www.aljazeera.com/xml/rss/all.xml',
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        reuters = Reuters('https://www.reuters.com/world')

        news = RSSNews(RSS_Links)

        # news = {**reuters.urls, **rss_news.urls}
        news.urls.update(reuters.urls)
        print(reuters.urls)

        if news.urls:
            for url, date in news.urls.items():
                article = NewsPlease.from_url(url)

                a = Article()

                a.author = 'Anonymous' if not article.authors else ', '.join(article.authors)
                a.title = article.title
                a.short_text = article.description
                a.content = article.maintext
                a.date = date
                a.source_link = url
                a.img = article.image_url
                a.save()
                bot.send_message(a)

        self.stdout.write(self.style.SUCCESS('Success'))
