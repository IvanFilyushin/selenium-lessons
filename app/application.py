from selenium import webdriver
from pages.main_page import MainPage
from pages.article_page import ArticlePage
from pages.basket_page import BasketPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.article_page = ArticlePage(self.driver)
        self.basket_page = BasketPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_new_article(self):
        self.main_page.open()
        self.main_page.select_random_article()
        self.article_page.add_to_basket()

    def get_basket_size(self):
        self.main_page.open()
        return self.main_page.how_many_articles_in_basket()

    def delete_articles(self):
        self.main_page.open()
        self.basket_page.empty_basket()
