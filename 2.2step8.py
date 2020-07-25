from selenium import webdriver
import os

#Открыть страницу.
brw = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
brw.get(link)

#Заполнить текстовые поля: имя, фамилия, email
brw.find_element_by_name("firstname").send_keys('Lera')
brw.find_element_by_name("lastname").send_keys('Sobaka')
brw.find_element_by_name("email").send_keys('LeraSobaka@dog.com')

#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'dog.txt')           # добавляем к этому пути имя файла

brw.find_element_by_css_selector("#file").send_keys(file_path)  #отправляем

brw.find_element_by_css_selector('.btn').click()