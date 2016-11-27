"""
Проверка открытия правильной страницы
(с дополнительными проверками значений и стилей)
"""

from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://localhost/litecart/en/")

regular_price = "s.regular-price"
campaign_price = "strong.campaign-price"

l = wd.find_element_by_css_selector("div#box-campaigns li.product.column.shadow.hover-light")
article = l.find_element_by_css_selector("a")
href = article.get_attribute("href")

name = l.find_element_by_css_selector("a div.name").get_attribute("textContent")
price = l.find_element_by_css_selector(regular_price).get_attribute("textContent")
font_size = l.find_element_by_css_selector(regular_price).value_of_css_property("font-size")
color_price = l.find_element_by_css_selector(regular_price).value_of_css_property("color")
cam_price = l.find_element_by_css_selector(campaign_price).get_attribute("textContent")
font_size_cam_price = l.find_element_by_css_selector(campaign_price).value_of_css_property(
    "font-size")
color_price_cam = l.find_element_by_css_selector(campaign_price).value_of_css_property(
    "color")

article.click()

nameN = wd.find_element_by_css_selector("h1.title").text
priceN = wd.find_element_by_css_selector(regular_price).get_attribute("textContent")
cam_priceN = wd.find_element_by_css_selector(campaign_price).get_attribute("textContent")
color_priceN = wd.find_element_by_css_selector(regular_price).value_of_css_property("color")
color_price_camN = wd.find_element_by_css_selector(campaign_price).value_of_css_property("color")
font_sizeN = wd.find_element_by_css_selector(regular_price).value_of_css_property("font-size")
font_size_cam_priceN = wd.find_element_by_css_selector(campaign_price).value_of_css_property("font-size")

print("Элементы: на главной странице - на странице товара:")
print("names: %s - %s" % (name, nameN))
print("price: %s - %s" % (price, priceN))
print("cam_price: %s - %s" % (cam_price, cam_priceN))
print("color reg price: %s - %s" % (color_price, color_priceN))
print("color cam price: %s - %s" % (color_price_cam, color_price_camN))
print("font-size reg: %s - %s" % (font_size, font_sizeN))
print("font-size cam: %s - %s" % (font_size_cam_price, font_size_cam_priceN))

wd.close()
