import time

from django.test import LiveServerTestCase
from selenium import webdriver
from django.core.management import call_command



# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:\\bin\\chromedriver.exe')

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

    # TODO Message: no such element: Unable to locate element: {"method":"css selector","selector":".nav-link active"}
    def test_navbar_item(self):
        self.browser.get(self.live_server_url)
        navbar_item = self.browser.find_element_by_class_name("nav-link active")
        print(navbar_item)
        time.sleep(500)
        self.assertEquals(navbar_item.text, 'Home')

    # TODO Call parser or add item 
    def test_links(self):
        call_command('parser')
        self.browser.get(self.live_server_url)
        all_links = []
        for a in self.browser.find_elements_by_xpath('.//a'):
            all_links.append(a.get_attribute('href'))

        for i in range(len(all_links)):
            response = self.browser.get(all_links[i])
            self.assertEquals(response.status_code, 200)

    def test_imgs(self):
        call_command('parser')
        self.browser.get(self.live_server_url)
        all_imgs = []
        for a in self.browser.find_elements_by_xpath('.//img'):
            all_imgs.append(a.get_attribute('src'))

        for i in range(len(all_imgs)):
            img = self.browser.get(all_imgs[i])
            self.assertIsNotNone(img)