import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# wd = webdriver.Firefox(firefox_binary=binary)

wd = webdriver.Chrome()
wd.get("http://localhost/litecart/en/")

articles_in_basket = int(wd.find_element_by_css_selector("span.quantity").text)

for i in range(3):
    # выбираем произвольный товар
    articles = wd.find_elements_by_css_selector("ul.listing-wrapper.products a.link")
    num_article = random.randint(0, len(articles) - 1)
    articles[num_article].click()
    WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, 'add_cart_product')))

    # если товар представлен разными размерами выбираем первый размер
    articles_with_size = wd.find_elements_by_css_selector("select[name='options[Size]'] option")
    if len(articles_with_size) > 0:
        articles_with_size[1].click()

    # добавляем товар в корзину
    wd.find_element_by_css_selector("button[value='Add To Cart']").click()
    articles_in_basket += 1
    WebDriverWait(wd, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(articles_in_basket)))

    # возвращаемся на главную страницу
    wd.find_element_by_css_selector("img[alt='My Store']").click()
    WebDriverWait(wd, 5).until(EC.title_contains("Online"))

# переходим на страницу управления корзиной и удадяем все товары
wd.find_element_by_css_selector("a[href='http://localhost/litecart/en/checkout'].link").click()

for i in range(articles_in_basket):
    WebDriverWait(wd, 7).until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
    wd.find_element_by_name('remove_cart_item').click()

# возвращаемся на главную страницу
wd.find_element_by_css_selector("a[href='http://localhost/litecart/en/']").click()
wd.close()
