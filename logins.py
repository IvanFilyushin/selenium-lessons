from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def login_admin():
    #binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    #wd = webdriver.Firefox(firefox_binary=binary)
    # wd = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()
    return wd
