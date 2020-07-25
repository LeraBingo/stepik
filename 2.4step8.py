from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

#Открыть страницу.
brw = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
brw.get(link)

#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
WebDriverWait(brw, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
#Нажать на кнопку "Book"
brw.find_element_by_id('book').click()

#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
x=int(brw.find_element_by_id('input_value').text)
res=str(log(abs(12*sin(x))))
brw.find_element_by_tag_name("input").send_keys(res)
brw.find_element_by_css_selector('#solve').click()