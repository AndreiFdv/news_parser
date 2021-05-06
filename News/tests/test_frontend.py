from django.core.management import call_command
from django.test import Client, LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:\\bin\\chromedriver.exe')
        self.client = Client()

    def tearDown(self):
        self.browser.close()

    def test_title(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        self.assertIn('Ddd News', title.title())

    def test_logo(self):
        self.browser.get(self.live_server_url)
        logo = self.browser.find_element_by_class_name('navbar-brand')
        self.assertIn(logo.text, 'DDD news')

    def test_links(self):
        call_command('parser')
        self.browser.get(self.live_server_url)
        links = [x.get_attribute('href') for x in self.browser.find_elements_by_tag_name('a')]

        for link in links:
            response = self.client.get(link)
            self.assertEquals(response.status_code, 200)

    def test_images(self):
        call_command('parser')
        self.browser.get(self.live_server_url)
        images = [x.get_attribute('src') for x in self.browser.find_elements_by_tag_name('img')]

        self.assertEquals(5, len(images))

    def test_articles(self):
        call_command('parser')
        self.browser.get(self.live_server_url)
        links = [x.get_attribute('href') for x in self.browser.find_elements_by_tag_name('a')]

        for link in links:
            self.browser.get("127.0.0.1:8000/"+link)
            text = self.browser.find_element_by_class_name('article').text
            self.assertIsNotNone(text)
