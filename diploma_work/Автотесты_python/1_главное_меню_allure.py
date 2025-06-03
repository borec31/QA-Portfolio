import pytest
import allure
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

# Фикстура для инициализации и закрытия браузера
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Открываем браузер на полный экран
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(30)
    yield driver
    print("Закрываем браузер")
    driver.quit()

# Параметризованный тест для каждого элемента меню
@pytest.mark.parametrize("item", menu_items)
@allure.title("Проверка кликабельности элемента меню: {item}")
def test_menu_item(driver, item):
    with allure.step(f"Переход на страницу: {url}"):
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body"))
        )

    with allure.step(f"Проверка элемента: {item}"):
        try:
            # Локатор для элемента меню в навигации
            locator = (By.XPATH, f"//div[@class='subTableColumn']//a[normalize-space(text())='{item}']")

            # Ждем, пока элемент станет кликабельным
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )

            # Проверяем, что элемент отображается
            assert element.is_displayed(), f"Элемент '{item}' не отображается на странице"

            # Кликаем по элементу
            with allure.step(f"Клик по элементу: {item}"):
                element.click()
                print(f"Элемент '{item}' успешно кликнут")

            # Ждем загрузки новой страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )

            # Проверяем изменение URL
            if item != "Главная":
                current_url = driver.current_url
                assert current_url != url, f"После клика на '{item}' URL не изменился (остался {url})"
            else:
                assert driver.current_url == url, f"После клика на 'Главная' URL изменился на {driver.current_url}"

        except Exception as e:
            # Сохраняем скриншот для отчета Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"error_screenshot_{item}",
                attachment_type=allure.attachment_type.PNG
            )
            print(f"Ошибка при обработке элемента '{item}': {str(e)}")
            pytest.fail(f"Не удалось обработать элемент '{item}': {str(e)}")