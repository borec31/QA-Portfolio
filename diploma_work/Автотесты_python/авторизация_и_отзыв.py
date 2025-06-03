import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


print("ОР:Инициализация  вебдрайвера")
link = "https://sew-irk.ru/"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
#Открытие браузера
browser.get(link)
print("ФР:Вебдрайвер инициализирован")

#вход в  личный  кабинет
print("Кликаем кнопку 'Вход' в шапке сайта")
step1 = browser.find_element(By.LINK_TEXT,"Вход").click()
print("ФР:Кнопка 'Вход' в шапке сайт кликнута")
#авторизация
print("ОР:Вводим логин")
step2 = browser.find_element(By.XPATH, "//input[@name='USER_LOGIN']").send_keys('klara@mail.ru')
print("ФР:Логин введен")
print("ОР:Вводим пароль")
step3=browser.find_element(By.XPATH, "//input[@name='USER_PASSWORD']").send_keys('йцукен12345')
print("ФР:Пароль введен")
print("ОР:Кликаем кнопку 'Войти'")
step4=browser.find_element(By.XPATH, "//div[@class='auth-submit-container']").click()
print("ОР:Кнопка 'Войти' нажата, произошел переход в личный  кабинет")
time.sleep (2)
print("скролим вниз до футера")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
print("скрол произошел успешно")
print("кликаем кнопку отзывы  в  футере")
step5=browser.find_element(By.LINK_TEXT, "Отзывы").click()
print("кликаем кнопку отзывы  в  футере")
time.sleep(2)
print("клик прошел успешно,произошел переход на страницу с  отзывами")
step6=browser.find_element(By.LINK_TEXT, "Оставить отзыв").click()
time.sleep(2)
print("кликаем кнопку 'оставить отзыв'")
step7=browser.find_element(By.XPATH, "//select[@name='review-rating']").click()
time.sleep(1)
print("клик прошел успешно, произошел скрол вниз страницы к полю 'добавить  отзыв'")
step8=browser.find_element(By.XPATH, "//option[@value='4']").click()
time.sleep(1)
print("заполнение отзыва'")
step9=browser.find_element(By.XPATH, "//textarea[@name='review-text']").send_keys("Мне все нравится")
time.sleep(2)
print("Отзыв заполнен")
print("Кликнуть кнопку 'оставить отзыв'")
step9=browser.find_element(By.XPATH, "//input[@class='shop-review-form-submit']").click()
print("Отзыв отправлен")
time.sleep(2)
print("Тест пройден успешно")