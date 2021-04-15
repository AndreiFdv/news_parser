import re

import feedparser
import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse

from News.models import Article


def link_exists(link: str) -> bool:
    return Article.objects.filter(source_link=link).exists()


class Reuters:
    def __init__(self, url: str):
        html = requests.get(url)
        soup = bs(html.content, "html.parser")
        self.links = soup.find_all('div', {'class': re.compile(r'StoryCollection__(story|hero).*')})
        self.urls = self.get_urls()

    def get_urls(self) -> list:
        urls = list()
        reuters = 'https://www.reuters.com'
        for link in self.links[:5]:
            href = link.a['href']
            if not link_exists(reuters + href):
                urls.append(reuters + href)
        return urls


class RSSNews:
    def __init__(self, links: list):
        self.links = links
        self.urls = self.get_urls()

    def get_urls(self):
        urls = dict()

        for link in self.links:
            feed = feedparser.parse(link)

            for entry in feed['entries'][:5]:
                if not link_exists(entry['link']):
                    urls.update({entry['link']: parse(entry['published'])})

        return urls
