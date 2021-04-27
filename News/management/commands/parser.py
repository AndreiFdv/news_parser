from django.core.management.base import BaseCommand
from newspaper import Article as NewsArticle

from News.management.commands import bot
from News.models import Article
from News.news_sites import Reuters, RSSNews

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

        if news.urls:
            for url, date in news.urls.items():
                article = NewsArticle(url)
                article.download()
                article.parse()

                a = Article()

                a.author = 'Anonymous' if not article.authors else ', '.join(article.authors)
                a.title = article.title
                a.short_text = article.meta_description
                a.content = article.text
                a.date = date
                a.source_link = url
                a.img = article.top_img

                a.save()
                bot.send_message(a)

        self.stdout.write(self.style.SUCCESS('Success'))
