from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # Вход в систему
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Выбор товара и добавление в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Проверка, что товар добавлен в корзину
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Товар не добавлен в корзину!"

    time.sleep(2)  # Для демонстрации


if __name__ == "__main__":
    pytest.main(["-v"])
