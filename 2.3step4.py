from selenium import webdriver
from math import log, sin

#Открыть страницу.
brw = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
brw.get(link)

#Нажать на кнопку
brw.find_element_by_tag_name("button").click()

#Принять confirm
confirm = brw.switch_to.alert
confirm.accept()

#На новой странице решить капчу для роботов, чтобы получить число с ответом
x=int(brw.find_element_by_css_selector("#input_value").text)
res=str(log(abs(12*sin(x))))
brw.find_element_by_tag_name("input").send_keys(res)

brw.find_element_by_css_selector('.btn').click()