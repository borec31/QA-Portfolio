# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait #ожидание  рендера(отрисовка  элемента  на  странице)
# from selenium.webdriver.support import expected_conditions as EC #исключительное  ожидание
# from  selenium.webdriver.chrome.service  import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# print("задаем стартовую страницу")
# link="https://sew-irk.ru/"
#
# print("определяем  браузер")
# browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# browser.maximize_window()
# print("переходим  на  стартовую  страницу")
# browser.get(link)
# #--------------------------
# print("задаем  список  элементов  для  проверки")
# name_webtucre_10_el=["Главная","Каталог","Оплата","Доставка","Оптовикам","Магазины","Акции","Школа шитья","Вход","Регистрация","Иркутск"]
#
# proverka_name = []
# print("перебираем по  порядку элементы  списка")
# for element_name in name_webtucre_10_el:
#     locator = (By.XPATH, f"//div[@class='subTableColumn']//*[text()='{element_name}']")
#     print(f"находим и  кликаем элемент {element_name}")
#     try:
#         element=WebDriverWait(browser,10).until(EC.element_to_be_clickable(locator)).click()
#         #print(f"добавляем элемент {element_name} в  список  proverka_name")
#         proverka_name.append(element_name)
#
#     except Exception as e:
#         print(f"'{element_name}:{e}'")
#         print("выводим сообщение  об  ошибке")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Список элементов меню для проверки
menu_items = [
    "Главная", "Каталог", "Оплата", "Доставка", "Оптовикам",
    "Магазины", "Акции", "Школа шитья", "Вход", "Регистрация"
]

# Стартовая страница
url = "https://sew-irk.ru/"

# Инициализация браузера
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Открываем браузер на полный экран
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Устанавливаем таймаут для загрузки страницы
    driver.set_page_load_timeout(30)

    # Переходим на стартовую страницу
    print(f"Переходим на страницу: {url}")
    driver.get(url)

    # Ждем, пока страница полностью загрузится
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body"))
    )

    # Список для хранения успешно найденных элементов
    found_items = []

    # Перебираем элементы меню
    for item in menu_items:
        print(f"Проверяем элемент: {item}")
        try:
            # Локатор для элемента меню в навигации
            locator = (By.XPATH, f"//div[@class='subTableColumn']//a[normalize-space(text())='{item}']")

            # Ждем, пока элемент станет кликабельным
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )

            # Кликаем по элементу
            element.click()
            print(f"Элемент '{item}' успешно кликнут")

            # Добавляем элемент в список найденных
            found_items.append(item)

            # Ждем загрузки новой страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )

            # Возвращаемся на главную страницу
            print(f"Возвращаемся на главную страницу: {url}")
            driver.get(url)

            # Ждем, пока главная страница снова загрузится
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )

        except Exception as e:
            print(f"Ошибка при обработке элемента '{item}': {str(e)}")

    # Выводим результат
    print("\nРезультат проверки:")
    print(f"Успешно найдено и кликнуто элементов: {len(found_items)} из {len(menu_items)}")
    print(f"Найденные элементы: {found_items}")

finally:
    # Закрываем браузер
    print("Закрываем браузер")
    driver.quit()
