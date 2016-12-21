from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasketPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def go_to_basket(self):
        self.driver.get("http://localhost/litecart/en/checkout")

    @property
    def get_num_of_articles(self):
        return len(self.driver.find_elements_by_css_selector(".dataTable.rounded-corners tbody>tr"))-5

    @property
    def delete_article(self):
        self.driver.find_element_by_name('remove_cart_item').click()

    def empty_basket(self):
        self.go_to_basket
        while self.get_num_of_articles>0:
            WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
            self.delete_article



