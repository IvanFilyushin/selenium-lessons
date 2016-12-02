"""

Добавление товара

"""
from logins import login_admin
import random

wd = login_admin()
wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")

wd.find_element_by_css_selector("a[href$='edit_product']").click()

# General

name = "BanDuck" + str(random.randint(0, 99))

wd.find_element_by_css_selector("input[name='status'][value='1']").click()
wd.find_element_by_css_selector("input[name='name[en]']").send_keys(name)
wd.find_element_by_css_selector("input[name='code']").send_keys('123')
wd.find_element_by_css_selector("input[data-name='Rubber Ducks']").click()
wd.find_element_by_css_selector("input[name='product_groups[]'][value='1-3']").click()
wd.find_element_by_css_selector("input[name='quantity']").clear()
wd.find_element_by_css_selector("input[name='quantity']").send_keys('10')
wd.find_element_by_css_selector("select[name='sold_out_status_id']").click()
wd.find_element_by_css_selector("input[name='new_images[]']") \
    .send_keys("C:\\xampp\htdocs\\litecart\\images\\products\\1-yellow-duck-1.png")
wd.find_element_by_css_selector("input[name='date_valid_from']").send_keys("02.12.2016")
wd.find_element_by_css_selector("input[name='date_valid_to']").send_keys("02.12.2017")

# Information

wd.find_element_by_css_selector("a[href='#tab-information']").click()
wd.find_element_by_css_selector("select[name='manufacturer_id'] option[value='1']").click()
wd.find_element_by_css_selector("input[name='keywords']").send_keys(name)
wd.find_element_by_css_selector("input[name='short_description[en]']").send_keys("%s" % (name * 3))
wd.find_element_by_css_selector("div.trumbowyg-editor").send_keys("Duuuuuuuuuuuuuuuck")

# Prices
wd.find_element_by_css_selector("a[href='#tab-prices']").click()
price = wd.find_element_by_css_selector("input[name='purchase_price']")
price.clear()
price.send_keys(random.randint(10, 10))
wd.find_element_by_css_selector("select[name='purchase_price_currency_code'] option[value='USD']").click()

price = wd.find_element_by_css_selector("input[name='prices[USD]']")
price.clear()
price.send_keys(random.randint(10, 20))

price = wd.find_element_by_css_selector("input[name='prices[EUR]']")
price.clear()
price.send_keys(random.randint(12, 25))

# Добавление товара в католог
wd.find_element_by_css_selector("button[name='save']").click()

# Проверка наличия добавленного товара в каталоге

articles = wd.find_elements_by_css_selector("table.dataTable tr.row td a")
if not (name in [article.text for article in articles]):
    print("Товара %s нет" % name)

wd.close()
