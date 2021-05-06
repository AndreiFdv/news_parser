import time
from django.test import LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class Main(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/x/PycharmProjects/SE_Project/News/tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_this(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        logo = self.browser.find_element_by_class_name('navbar-brand')
        navbar_item = self.browser.find_element_by_class_name('nav-link active')
        self.assertEquals(title, 'DDD news')
        self.assertEquals(logo, 'DDD news')
        self.assertEquals(navbar_item, 'Home')

        all_links = []
        for a in self.browser.find_elements_by_xpath('.//a'):
            print(a.get_attribute('href'))
            all_links.append(a.get_attribute('href'))
        time.sleep(10)
