from selenium.webdriver.chrome.webdriver import WebDriver
import math


# прописываем функцию для подсчета значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# открываем браузер
con = WebDriver()

# открываем целевую страницу
con.get(" http://suninjuly.github.io/get_attribute.html")

# находим веб-элемент x
web_element_x = con.find_element_by_css_selector("#treasure").get_attribute("valuex")

# находим значение для ввода
value = calc(web_element_x)

# находим элементы текстовое поле, чекбокс, радио-кнопку, кнопку "отправить"
text_field = con.find_element_by_css_selector("#answer")
checkbox = con.find_element_by_css_selector("#robotCheckbox")
radio_btn = con.find_element_by_css_selector("#robotsRule")
submit_btn = con.find_element_by_css_selector('[type="submit"]')

# вводим значение в текстовое поле
text_field.send_keys(value)

# отмечаем чекбокс
checkbox.click()

# выбираем значение радио-кнопки
radio_btn.click()

# нажимаем на кнопку "отправить"
submit_btn.click()

# закрываем браузер
