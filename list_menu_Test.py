from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Chrome()
wd.get("http://localhost/litecart/admin/")
wd.find_element_by_name("username").send_keys("admin")
wd.find_element_by_name("password").send_keys("admin")
wd.find_element_by_name("login").click()

size = len(wd.find_elements_by_css_selector("ul#box-apps-menu li#app-"))

for l in range(size):
    wd.find_elements_by_css_selector("ul#box-apps-menu li#app-")[l].click()
    title = WebDriverWait(wd, 1).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1")))
    print(title.text)
    if len(wd.find_elements_by_css_selector("ul#box-apps-menu li.selected ul li")) != 0:
        elements = len(wd.find_elements_by_css_selector("ul#box-apps-menu li.selected ul li"))
        for e in range(elements):
            wd.find_elements_by_css_selector("ul#box-apps-menu li.selected ul li")[e].click()
            title = WebDriverWait(wd, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1")))
            print(title.text)
wd.close()
