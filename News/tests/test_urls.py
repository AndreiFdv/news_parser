from django.test import SimpleTestCase
from django.urls import resolve, reverse

from News.views import DetailView, IndexView


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('News:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_detail_url_resolves(self):
        url = reverse('News:detail', args='1')
        self.assertEquals(resolve(url).func.view_class, DetailView)
