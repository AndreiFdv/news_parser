from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from News.models import Article, TelegramUser


class TestModels(TestCase):

    def setUp(self):
        self.datetime = timezone.now()
        self.article = Article.objects.create(
            title='Test',
            date=self.datetime,
            author='Author',
            content='Test Text',
            short_text='Short Text',
            source_link='link',
            img='img_link',
        )
        self.telegram_user = TelegramUser.objects.create(
            user_id=1337,
            user_name='Test Name'
        )

    def test_article_fields(self):
        self.assertEquals(self.article.title, 'Test')
        self.assertEquals(self.article.date, self.datetime)
        self.assertEquals(self.article.author, 'Author')
        self.assertEquals(self.article.content, 'Test Text')
        self.assertEquals(self.article.short_text, 'Short Text')
        self.assertEquals(self.article.source_link, 'link')
        self.assertEquals(self.article.img, 'img_link')

    def test_telegram_user_fields(self):
        self.assertEquals(self.telegram_user.user_id, 1337)
        self.assertEquals(self.telegram_user.user_name, 'Test Name')

    def test_article_str_return_value(self):
        self.assertEquals(self.article.title, str(self.article))

    def test_telegram_user_str_return_value(self):
        self.assertEquals(self.telegram_user.user_name, str(self.telegram_user))

    def test_article_get_absolute_url_value(self):
        self.assertEquals(self.article.get_absolute_url(), reverse('News:detail', args=[self.article.id]))
