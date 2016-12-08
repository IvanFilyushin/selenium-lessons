import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logins import login_admin


def wait_new_window(wd, old_windows):
    while True:
        windows = wd.window_handles
        new = list(set(windows) - set(old_windows))
        if len(new)>0:
            return new[0]


wd = login_admin()

wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
rows = wd.find_elements_by_css_selector(".row")
random_country = random.randint(1, len(rows) - 1)
# на этой строчке Ie выбрасывает ошибку Message: An invalid or illegal selector was specified
rows[random_country].find_element_by_css_selector("td:nth-child(5) a").click()
WebDriverWait(wd, 5).until(EC.title_contains("Edit"))
hrefs = wd.find_elements_by_css_selector("form a[target='_blank']")

for href in hrefs:
    main_window = wd.current_window_handle
    old_windows = wd.window_handles
    href.click()
    new_window = wait_new_window(wd, old_windows)
    wd.switch_to_window(new_window)
    wd.close()
    wd.switch_to_window(main_window)
# в FF это строчка не закрывает окно
wd.close()

