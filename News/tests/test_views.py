from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from News.models import Article


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('News:index')
        self.article = Article.objects.create(
            title='Test',
            date=timezone.now()
        )
        self.detail_url = reverse('News:detail', args=[self.article.id])

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')

    def test_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/article.html')
