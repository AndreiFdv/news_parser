import time

from django.test import LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('c:\\bin\\chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_this(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        self.assertEquals(title, 'DDD news')
        time.sleep(20)
