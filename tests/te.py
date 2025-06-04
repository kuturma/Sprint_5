import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import Locators
from data_generate_and_static_data.data_generate_and_static_data import generate_email, generate_name, generate_password, generate_short_password, UserData 
from .conftest import driver

BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestStellarBurgers:
    

#            ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР

# Проверяем переход из личного кабинета в конструктор по кнопке "Конструктор" и логотипу сайта
# Создаём параметризацю для перехода по разным элементам на странице из личного кабинета
    @pytest.mark.parametrize("element", [Locators.LINK_CONSTRUCTOR, Locators.LOGO])
    def test_return_to_constructor(self, driver, element):
        driver.get(BASE_URL)

        # Кликаем по кнопке "Личный кабинет" в шапке сайта
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys(*UserData.email)
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys(*UserData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по нужному элементу (логотип или "Конструктор")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element)).click()

        # Проверяем, что перешли на главную
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{BASE_URL}/"))
        assert driver.current_url == f"{BASE_URL}/"