from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from faker import Faker
import time

fake = Faker(["ru_RU"])
print("ОР: Инициализация  вебдрайвера")
link = "https://sew-irk.ru/"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
browser.get(link)
print("ФР: Вебдрайвер инициализирован")

print("ОР:Ввод товара  в  поисковую строку")
step5=browser.find_element(By.ID, "searchQuery").send_keys('Ножницы AURORA раскройные 27см')
print("ФР:Товар введен  в  поисковую строку")
print("ОР:Кликнуть  на  стрелочку  в  поисковой строке")
step6=browser.find_element(By.XPATH, "//input[@name='send']").click()
print("ФР:Стрелочка кликнута")
print("ОР:Выбираем количество товара 2, нажимая на  +")
step6=browser.find_element(By.XPATH, "//a[@class='plus']").click()
time.sleep(2)
print("ФР:Выбрано количество товара 2")
print("ОР:Добавляем товар  в  корзину")
step7 = browser.find_element(By.XPATH, "//a[@class='addCart changeID changeQty changeCart']").click()
print("ФР: Товар добавлен в  корзину")
time.sleep(2)
print("ОР:Переходим  в  корзину")
step8 =browser.find_element(By.LINK_TEXT, "Перейти в корзину").click()
print("ФР:Переход  в  корзину осуществлен")
time.sleep(2)
print("ОР: нажимаeм  на  кнопку'оформить  заказ'")
step9 = browser.find_element(By.XPATH, "//a[@class='btn-simple btn-medium goToOrder']").click()
print("ФР: Кнопка'оформить  заказ' нажата")
print("ОР:нажать  на  кнопку 'физическое лицо'")
step10 = browser.find_element(By.XPATH, "//label[@class='btn-person-type']").click()
print("ФР: Кнопка 'физическое лицо' нажата")

phone = fake.phone_number()

time.sleep(2)
print("ОР:Заполняем обязательные поля")
field = browser.find_element(By.ID, 'soa-property-1').send_keys("Алла")
field = browser.find_element(By.ID, 'soa-property-2').send_keys("alla@mail.ru")
field = browser.find_element(By.ID, 'soa-property-3').send_keys(phone)
print("ФР:Обязательные поля заполнены")
time.sleep(2)
print("ОР: Нажать на  кнопку ' оформить  заказ'")
step11 = browser.find_element(By.LINK_TEXT, 'Оформить заказ').click()
print("ФР: заказ оформлен")
print("Тест успешно пройден")
time.sleep(2)


