from selenium import webdriver
from math import log, sin

#Открыть страницу.
brw = webdriver.Chrome()
link = " http://suninjuly.github.io/redirect_accept.html"
brw.get(link)

#Нажать на кнопку
brw.find_element_by_tag_name('button').click()

#Переключиться на новую вкладку. Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
#который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
window_name = brw.window_handles[1]
brw.switch_to.window(window_name)

#Пройти капчу для робота и получить число-ответ
x=int(brw.find_element_by_id('input_value').text)
res=str(log(abs(12*sin(x))))
brw.find_element_by_tag_name("input").send_keys(res)
brw.find_element_by_css_selector('.btn').click()
