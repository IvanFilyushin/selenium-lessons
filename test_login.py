import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    # binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # wd = webdriver.Firefox(firefox_binary=binary)
    wd = webdriver.Chrome()
    print(wd.capabilities)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):

    driver.get("http://localhost/litecart/admin/")

    # login
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "platform")))

    #points(driver)
    # logout
    driver.find_element_by_xpath('//a[@href="http://localhost/litecart/admin/logout.php"]').click()

