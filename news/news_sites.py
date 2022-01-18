import feedparser
from dateutil.parser import parse

from news.models import Article


def link_exists(link: str) -> bool:
    return Article.objects.filter(source_link=link).exists()


class RSSNews:
    def __init__(self, links: list):
        self.links = links
        self.urls = self.get_urls()

    def get_urls(self) -> dict:
        urls = dict()

        for link in self.links:
            feed = feedparser.parse(link)

            for entry in feed['entries'][:1]:
                e_link = entry['link'] if not feed['feed'].title == 'FOX News' else entry['id']
                if not link_exists(e_link):
                    urls.update({e_link: parse(entry['published'])})

        return urls
