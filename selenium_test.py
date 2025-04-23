from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_login_form():
    # Настройка WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Открытие тестовой страницы
        driver.get("https://www.saucedemo.com/")

        # Нахождение полей ввода и кнопки
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Ввод данных
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Проверка успешного входа
        time.sleep(2)  # Ожидание загрузки страницы
        inventory_page = driver.find_element(By.CLASS_NAME, "inventory_list")
        assert inventory_page.is_displayed(), "Login failed: Inventory page not displayed"

        print("Test passed: Successfully logged in and inventory page displayed")

    except Exception as e:
        print(f"Test failed: {str(e)}")

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_login_form()
