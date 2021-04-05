import feedparser
import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse


class Reuters:
    def __init__(self, url: str):
        html = requests.get(url)
        soup = bs(html.content, "html.parser")
        self.links = soup.find_all('div', {'class': 'story-content'})
        self.urls = self.get_urls()

    def get_urls(self) -> list:
        urls = list()
        for link in self.links:
            urls.append('https://www.reuters.com' + link.a['href'])
        return urls


class RSSNews:
    def __init__(self, links: list):
        self.links = links
        self.urls = self.get_urls()

    def get_urls(self):
        urls = dict()

        for link in self.links:
            feed = feedparser.parse(link)

            for entry in feed['entries']:
                urls.update({entry['link']: parse(entry['published'])})

        return urls
