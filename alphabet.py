"""
Проверка, что страны расположены в алфавитном порядке

"""

from logins import login_admin

wd = login_admin()
wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

contries = wd.find_elements_by_css_selector("table.dataTable a:not([title])")
name = [c.get_attribute("innerText") for c in contries]
nameS = name
nameS.sort()
if name != nameS:
    print("Список неотсортирован!")
wd.close()
