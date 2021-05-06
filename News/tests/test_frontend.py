import time

from django.core.management import call_command
from django.test import LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:\\bin\\chromedriver.exe')
        call_command('parser')

    def tearDown(self):
        self.browser.close()

    def test_title(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        self.assertIn('Ddd News', title.title())

    def test_logo(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        logo = self.browser.find_element_by_class_name('navbar-brand')
        self.assertIn(logo.text, 'DDD news')

    def test_links(self):
        self.browser.get(self.live_server_url)
        links = [x.get_attribute('href') for x in self.browser.find_elements_by_tag_name('a')]
        self.assertEquals(7, len(links))

    def test_images(self):
        self.browser.get(self.live_server_url)
        images = [x.get_attribute('src') for x in self.browser.find_elements_by_tag_name('img')]

        self.assertEquals(5, len(images))
