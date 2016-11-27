"""
Проверка, что зоны расположены в алфавитном порядке для geo_zones

"""

from logins import login_admin

wd = login_admin()
wd.get("http://localhost/litecart/admin/?app=geo_zones")
contry_with_zones = []
nrows = len(wd.find_elements_by_css_selector(".row"))
for r in range(nrows):
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=%s" % str(r + 1))
    zones = wd.find_elements_by_css_selector("table#table-zones td:nth-child(3) [selected=selected]")
    name = ([p.text for p in zones])
    nameS = name
    nameS.sort()
    if name != nameS:
        print("Список неотcортирован!")

wd.close()
