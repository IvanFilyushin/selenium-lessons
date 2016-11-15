import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
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

    # выбор Settings
    driver.find_element_by_xpath('//a[@href="http://localhost/litecart/admin/?app=settings&doc=store_info"]').click()
    WebDriverWait(driver, 1).until(EC.title_contains("Settings"))

    # logout
    driver.find_element_by_xpath('//a[@href="http://localhost/litecart/admin/logout.php"]').click()
