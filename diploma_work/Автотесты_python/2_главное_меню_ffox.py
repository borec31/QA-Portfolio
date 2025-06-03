from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service  # Изменено на Firefox Service
from webdriver_manager.firefox import GeckoDriverManager  # Изменено на GeckoDriverManager

print("задаем стартовую страницу")
link = "https://sew-irk.ru/"

print("определяем браузер")
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # Изменено на Firefox
browser.maximize_window()
print("переходим на стартовую страницу")
browser.get(link)
#--------------------------
print("задаем список элементов для проверки")
name_webtucre_10_el = ["Главная", "Каталог", "Оплата", "Доставка", "Оптовикам", "Магазины", "Акции", "Школа шитья", "Вход", "Регистрация", "Казань"]

proverka_name = []
print("перебираем по порядку элементы списка")
for element_name in name_webtucre_10_el:
    locator = (By.XPATH, f"//div[@class='subTableColumn']//*[text()='{element_name}']")
    print(f"находим и кликаем элемент {element_name}")
    try:
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator)).click()
        proverka_name.append(element_name)
    except Exception as e:
        print(f"'{element_name}:{e}'")
        print("выводим сообщение об ошибке")

browser.quit()  # Закрытие браузера



