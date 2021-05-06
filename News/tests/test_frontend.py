import time
from django.test import LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_title(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        self.assertEquals(title, 'DDD news')

    def test_logo(self):
        self.browser.get(self.live_server_url)
        logo = self.browser.find_element_by_class_name('navbar-brand')
        self.assertEquals(logo, 'DDD news')

    def test_navbar_item(self):
        self.browser.get(self.live_server_url)
        navbar_item = self.browser.find_element_by_class_name('nav-link active')
        self.assertEquals(navbar_item, 'Home')

    def tes_links(self):

        self.browser.get(self.live_server_url)
        all_links = []
        for a in self.browser.find_elements_by_xpath('.//a'):
            all_links.append(a.get_attribute('href'))

        for i in range(len(all_links)):
          response = self.browser.get(all_links[i])
          self.assertEquals(response.status_code, 200)
