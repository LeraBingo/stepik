from selenium.webdriver.chrome.webdriver import WebDriver
import math
from selenium.webdriver.support.ui import Select

# открываем браузер
brw= WebDriver()

# открываем целевую страницу
brw.get("http://suninjuly.github.io/selects1.html")

#Посчитать сумму заданных чисел
n1=int(brw.find_element_by_css_selector("#num1").text)
n2=int(brw.find_element_by_css_selector("#num2").text)
sum=str(n1+n2)

#Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(brw.find_element_by_tag_name("select"))  #Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select
select.select_by_visible_text(sum)  # ищем элемент с текстом "Python"

#Нажать кнопку "Submit"
brw.find_element_by_tag_name('button').click()
