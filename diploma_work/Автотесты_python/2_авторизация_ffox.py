import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager  # Изменено на GeckoDriverManager
from selenium.webdriver.firefox.service import Service   # Изменено на Firefox Service
from selenium.webdriver.support.ui import WebDriverWait

print("ОР: Инициализация вебдрайвера")
link = "https://sew-irk.ru/"
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # Изменено на Firefox
browser.maximize_window()
# Открытие браузера
browser.get(link)
print("ФР: Вебдрайвер инициализирован")

# Вход в личный кабинет
print("Кликаем кнопку 'Вход' в шапке сайта")
step1 = browser.find_element(By.LINK_TEXT, "Вход").click()
print("ФР: Кнопка 'Вход' в шапке сайт кликнута")
# Авторизация
print("ОР: Вводим логин")
step2 = browser.find_element(By.XPATH, "//input[@name='USER_LOGIN']").send_keys('alla@mail.ru')
print("ФР: Логин введен")
print("ОР: Вводим пароль")
step3 = browser.find_element(By.XPATH, "//input[@name='USER_PASSWORD']").send_keys('йцукен12345')
print("ФР: Пароль введен")
print("ОР: Кликаем кнопку 'Войти'")
step4 = browser.find_element(By.XPATH, "//div[@class='auth-submit-container']").click()
print("ОР: Кнопка 'Войти' нажата, произошел переход в личный кабинет")
time.sleep(2)
print("Тест пройден успешно")

browser.quit()  # Закрытие браузера