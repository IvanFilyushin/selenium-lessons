"""
Регистрация 


"""


from selenium import webdriver
import random
import rstr

email = 'user%s@ya.ru' % (str(random.randint(0, 99)))

form = {'firstname': 'Semen', 'lastname': 'Petrov', 'address1': 'Green Street', 'address2': 'Black alley',
        'city': 'Moscow', 'email': email, 'phone': '903', 'password': 'password', 'confirmed_password': 'password'}

wd = webdriver.Chrome()
wd.get("http://localhost/litecart/en/")

# на страницу регистрации
wd.find_element_by_css_selector("a[href='http://localhost/litecart/en/create_account']").click()

# заполняем все обязательные поля кроме Country,Postcode, Zones
for field in form.keys():
    wd.find_element_by_name(field).send_keys(form[field])

# снимаем чек-бокс Newsletter
wd.find_element_by_name('newsletter').click()

# выбираем произвольную страну Country из списка стран
wd.find_element_by_css_selector("span.select2-selection__rendered").click()
countries = wd.find_elements_by_css_selector("span.select2-results li")
wd.find_element_by_css_selector("input.select2-search__field").\
    send_keys(countries[random.randint(0, len(countries))].text)

wd.find_element_by_css_selector("span.select2-results li").click()

# вводим Postcode для выбранной страны
post_pattern = wd.find_element_by_name("postcode").get_attribute("pattern")
wd.find_element_by_name("postcode").send_keys(rstr.xeger(post_pattern))

# выбираем произвольное Zone для выбранной страны
wd.find_element_by_css_selector("select[name='zone_code']").click()
zones = wd.find_elements_by_css_selector("select[name='zone_code'] option")
if len(zones) > 0:
    zones[random.randint(0, len(zones))].click()

# создаём аккаунт и выходим
wd.find_element_by_name('create_account').click()
wd.find_element_by_link_text('Logout').click()

# вход с новым аккаунтом
wd.find_element_by_name('email').send_keys(form['email'])
wd.find_element_by_name('password').send_keys(form['password'])
wd.find_element_by_name('login').click()
wd.find_element_by_link_text('Logout').click()

wd.close()
