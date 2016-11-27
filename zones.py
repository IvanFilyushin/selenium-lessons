"""
Для тех стран, у которых количество зон отлично от нуля
-- проверка, что зоны расположены в алфавитном порядке

"""

from logins import login_admin

wd = login_admin()

wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

contry_with_zones = []
rows = wd.find_elements_by_css_selector(".row")
for r in rows:
    if '0' != r.find_element_by_css_selector("td:nth-child(6)").get_attribute("textContent"):
        contry_with_zones.append(r.find_element_by_css_selector("td:nth-child(4)").get_attribute("textContent"))

for c in contry_with_zones:
    wd.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=%s" % c)
    zones = wd.find_elements_by_css_selector("table#table-zones td:nth-child(3)")
    name = ([p.text for p in zones])
    nameS = name
    nameS.sort()
    if name != nameS:
        print("Список неотcортирован!")
wd.close()
