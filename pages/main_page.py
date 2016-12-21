from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


class MainPage:

    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def how_many_articles_in_basket(self):
        return int(self.driver.find_element_by_css_selector("span.quantity").text)

    @property
    def get_articles(self):
        return self.driver.find_elements_by_css_selector("ul.listing-wrapper.products a.link")

    def select_random_article(self):
        num_article = random.randint(0, len(self.get_articles) - 1)
        self.get_articles[num_article].click()

