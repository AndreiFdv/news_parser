from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from news.models import Article, TelegramUser


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

    def test_title(self):
        self.assertEquals(self.article.title, 'Test')

    def test_title_type(self):
        self.assertEquals(type(self.article.title), str)

    def test_date(self):
        self.assertEquals(self.article.date, self.datetime)

    def test_author(self):
        self.assertEquals(self.article.author, 'Author')

    def test_author_type(self):
        self.assertEquals(type(self.article.author), str)

    def test_content(self):
        self.assertEquals(self.article.content, 'Test Text')

    def test_content_type(self):
        self.assertEquals(type(self.article.content), str)

    def test_short_text(self):
        self.assertEquals(self.article.short_text, 'Short Text')

    def test_short_text_type(self):
        self.assertEquals(type(self.article.short_text), str)

    def test_link(self):
        self.assertEquals(self.article.source_link, 'link')

    def test_link_type(self):
        self.assertEquals(type(self.article.source_link), str)

    def test_img_link(self):
        self.assertEquals(self.article.img, 'img_link')

    def test_telegram_id(self):
        self.assertEquals(self.telegram_user.user_id, 1337)

    def test_telegram_id_type(self):
        self.assertEquals(type(self.telegram_user.user_id), int)

    def test_telegram_username(self):
        self.assertEquals(self.telegram_user.user_name, 'Test Name')

    def test_telegram_username_type(self):
        self.assertEquals(type(self.telegram_user.user_name), str)

    def test_article_str_return_value(self):
        self.assertEquals(self.article.title, str(self.article))

    def test_telegram_user_str_return_value(self):
        self.assertEquals(self.telegram_user.user_name, str(self.telegram_user))

    def test_article_get_absolute_url_value(self):
        self.assertEquals(self.article.get_absolute_url(), reverse('news:detail', args=[self.article.id]))
