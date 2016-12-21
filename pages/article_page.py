from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ArticlePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def get_num_of_articles(self):
        return int(self.driver.find_element_by_css_selector("span.quantity").text)

    @property
    def is_article_with_size(self):
        return len(self.driver.find_elements_by_css_selector("select[name='options[Size]'] option")) > 0

    @property
    def select_size(self):
        s  = self.driver.find_elements_by_css_selector("select[nae='options[Size]'] option")
        self.driver.find_elements_by_css_selector("select[name='options[Size]'] option")[1].click()

    @property
    def return_to_main_page(self):
        self.driver.find_element_by_css_selector("img[alt='My Store']").click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Online"))

    def add_to_basket(self):
        if self.is_article_with_size:
            self.select_size
        self.driver.find_element_by_css_selector("button[value='Add To Cart']").click()
        articles_in_basket = self.get_num_of_articles + 1
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(articles_in_basket)))
        self.return_to_main_page
