from selenium import webdriver

wd = webdriver.Chrome()
box = ['box-most-popular', 'box-campaigns', 'box-latest-products']
wd.get("http://localhost/litecart/en/")

for m in box:
    lists = wd.find_elements_by_css_selector("div#%s div.image-wrapper" % m)
    for s in lists:
        if len(s.find_elements_by_css_selector("div.sticker")) != 1:
            print('Должен быть один стикер в %s ' % m)
wd.close()
