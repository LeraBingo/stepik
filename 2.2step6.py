from selenium import webdriver
from math import log, sin

#Открыть страницу.
brw = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
brw.get(link)

#Считать значение для переменной x.
x=int(brw.find_element_by_css_selector('#input_value').text)

#Посчитать математическую функцию от x.
res=str(log(abs(12*sin(x))))
print(res)

#Проскроллить страницу вниз.
button = brw.find_element_by_tag_name("button")
brw.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#Ввести ответ в текстовое поле.
brw.find_element_by_css_selector('#answer').send_keys(res)

#Выбрать checkbox "I'm the robot".
cb=brw.find_element_by_css_selector('#robotCheckbox')
cb.click()

#Переключить radiobutton "Robots rule!".
brw.find_element_by_css_selector("#robotsRule").click()

#Нажать на кнопку "Submit".
brw.find_element_by_tag_name('button').click()