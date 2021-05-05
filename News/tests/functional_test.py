from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.utils import timezone
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# Create your tests here.
class Main(LiveServerTestCase):
  def setUp(self):
    self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    self.index_url = reverse('News:index')

    self.detail_url = reverse('News:detail', args=[self.article.id])
    self.logo = driver.find_element_by_class_name('navbar-brand')
    self.navbar_item = driver.find_element_by_class_name('nav-link active')

    self.all_links=[]
    for a in driver.find_elements_by_xpath('.//a'):
      print(a.get_attribute('href'))
      self.all_links.append(a.get_attribute('href'))



    # for i in range(len(all_links)):
    #   response = self.client.get(self.all_links[i])
    #   self.assertEquals(response.status_code, 200)
    #
