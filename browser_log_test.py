from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from logins import login_admin

wd = login_admin()

wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
# строки таблицы, содержащие каталог, подкаталоги и товары
rows=wd.find_elements_by_css_selector("table.dataTable tbody tr.row")
num = len(rows)
for i in range(num):
    refs = rows[i].find_elements_by_css_selector("a[href]")
    if len(refs) == 0:
        continue
    ref=refs[0].get_attribute("href")
    # для товара открываем страницу редактирования
    if ref.find("product_id")>0:
        refs[0].click()
        WebDriverWait(wd, 5).until(EC.title_contains("Edit"))
        # контролируем логи
        wd.get_log("browser")
        wd.find_element_by_name("cancel").click()
        WebDriverWait(wd, 5).until(EC.title_contains("Catalog"))
        rows = wd.find_elements_by_css_selector("table.dataTable tbody tr.row")
wd.close()