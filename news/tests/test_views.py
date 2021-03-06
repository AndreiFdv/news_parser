from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from news.models import Article


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('news:index')
        self.article = Article.objects.create(
            title='Test',
            date=timezone.now()
        )
        self.detail_url = reverse('news:detail', args=[self.article.id])

    def test_index_response_status(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'news/index.html')

    def test_detail_response_status(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_detail_template(self):
        response = self.client.get(self.detail_url)
        self.assertTemplateUsed(response, 'news/article.html')
