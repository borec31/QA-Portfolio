from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #ожидание  рендера(отрисовка  элемента  на  странице)
from selenium.webdriver.support import expected_conditions as EC #исключительное  ожидание
from  selenium.webdriver.chrome.service  import Service
from webdriver_manager.chrome import ChromeDriverManager


print("задаем стартовую страницу")
link="https://sew-irk.ru/"

print("определяем  браузер")
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
print("переходим  на  стартовую  страницу")
browser.get(link)
#--------------------------
print("задаем  список  элементов  для  проверки")
name_webtucre_10_el=["Главная","Каталог","Оплата","Доставка","Оптовикам","Магазины","Акции","Школа шитья","Вход","Регистрация","Иркутск"]

proverka_name = []
print("перебираем по  порядку элементы  списка")
for element_name in name_webtucre_10_el:
    locator = (By.XPATH, f"//div[@class='subTableColumn']//*[text()='{element_name}']")
    print(f"находим и  кликаем элемент {element_name}")
    try:
        element=WebDriverWait(browser,10).until(EC.element_to_be_clickable(locator)).click()
        #print(f"добавляем элемент {element_name} в  список  proverka_name")
        proverka_name.append(element_name)

    except Exception as e:
        print(f"'{element_name}:{e}'")
        print("выводим сообщение  об  ошибке")

