import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ..curl.curl import *
from ..locators.locators import Locators
from ..data_generate_and_static_data.data_generate_and_static_data import generate_email, generate_name, generate_password, generate_short_password, UserData 


class TestRegistration:   

#              РЕГИСТРАЦИЯ
    # Проверяем успешную регистрацию с помощью генератора случайных данных
    def test_successful_registration(self, driver):
        driver.get(url_register)
        name = generate_name()
        email = generate_email()
        password = generate_password()

        # Заполняем форму регистрации используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_NAME)).send_keys(name)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_EMAIL)).send_keys(email)
                                       
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_PASSWORD)).send_keys(password)

        # Нажимаем кнопку регистрации после того как она станет кликабельной
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_REGISTER)).click()

        # Проверяем, что перешли на страницу входа (есть поле email)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.INPUT_LOGIN_EMAIL))


    # Проверяем регистрацию с коротким паролем
    def test_registration_with_short_password(self, driver):
        driver.get(url_register)
        name = generate_name()
        email = generate_email()
        password = generate_short_password()

        # Заполняем форму регистрации через поиск элементов на странице регистрации
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

        # Нажимаем кнопку регистрации
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждём появления ошибки
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD))


class TestLoginFromDifferentPages:
#               ВХОД
# Проверяем успешный вход в систему из различных страниц сайта

    # Проверяем успешный вход в систему из перехода с главной страницы
    def test_login_from_various_paths_main_page(self, driver):
        # Переход на страницы через главную страницу
        driver.get(url)

        # Переходим на страницу входа через главную страницу
        driver.find_element(*Locators.LINK_LOGIN_MAIN).click()
       
        # Заполняем форму входа используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_EMAIL)).send_keys(*UserData.email)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_PASSWORD)).send_keys(*UserData.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()

        # Проверяем наличие кнопки "Оформить заказ" после входа
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


    # Проверяем успешный вход в систему из перехода со страницы личного кабинета
    def test_login_from_various_paths_login_page(self, driver):
        # Переход на страницы через указанные пути
        driver.get(url_login)

        # Так как мы уже находимся на странице входа, то перехоходить уже не нужно

        # Заполняем форму входа используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_EMAIL)).send_keys(*UserData.email)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_PASSWORD)).send_keys(*UserData.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()

        # Проверяем наличие кнопки "Оформить заказ" после входа
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


    # Проверяем успешный вход в систему из перехода со страницы регистрации
    def test_login_from_various_paths_register_page(self, driver):
        # Переход на страницы через указанные пути
        driver.get(url_register)
      
        # Переходим на страницу входа через страницу регистрации
        driver.find_element(*Locators.LINK_LOGIN_FROM_REGISTER).click()
   
        # Заполняем форму входа используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_EMAIL)).send_keys(*UserData.email)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_PASSWORD)).send_keys(*UserData.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()

        # Проверяем наличие кнопки "Оформить заказ" после входа
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


    # Проверяем успешный вход в систему из перехода со восстановления пароля
    def test_login_from_various_paths_forgot_password_page(self, driver):
        # Переход на страницы через указанные пути
        driver.get(url_forgot_password)

        # Переходим на страницу входа через страницу восстановления пароля
        driver.find_element(*Locators.LINK_LOGIN_FROM_FORGOT).click()

        # Заполняем форму входа используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_EMAIL)).send_keys(*UserData.email)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_PASSWORD)).send_keys(*UserData.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()

        # Проверяем наличие кнопки "Оформить заказ" после входа
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


class TestPersonalAccount:
#         ПЕРЕХОД В ЛИЧНЫЙ КАБИНЕТ

    # Проверяем переход в личный кабинет по кнопке в шапке сайта "Личный кабинет"
    def test_go_to_personal_account(self, driver):
        driver.get(url)

        # Ждём и кликаем по кнопке "Личный кабинет" в шапке сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN_HEADER)).click()
        
        #Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys(*UserData.email)
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys(*UserData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Проверяем, что появилась кнопка "Выйти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGOUT))


class TestReturnToConstructor:
#            ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР

    # Проверяем переход из личного кабинета в конструктор по кнопке "Конструктор"
    def test_return_to_constructor_on_the_constructor(self, driver):
        driver.get(url)

        # Кликаем по кнопке "Личный кабинет" в шапке сайта
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys(*UserData.email)
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys(*UserData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по элементу "Конструктор"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_CONSTRUCTOR)).click()

        # Проверяем, что перешли на главную
        WebDriverWait(driver, 5).until(EC.url_to_be(url))
        assert driver.current_url == url


    # Проверяем переход из личного кабинета в конструктор по кнопке логотипа сайта
    def test_return_to_constructor__on_the_logo(self, driver):
        driver.get(url)

        # Кликаем по кнопке "Личный кабинет" в шапке сайта
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys(*UserData.email)
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys(*UserData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по логотипу
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO)).click()

        # Проверяем, что перешли на главную
        WebDriverWait(driver, 5).until(EC.url_to_be(url))
        assert driver.current_url == url


class TestLogout:
#               ВЫХОД ИЗ АККАУНТА
    def test_logout(self, driver):
        driver.get(url)

        # Переходим в авторизацию через кнопку в шапке сайта "Личный кабинет"
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys(*UserData.email)
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys(*UserData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Переходим в личный кабинет через кнопку "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по "Выйти"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)).click()

        # Проверяем, что появилась кнопка "Войти" на экране
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGIN))


class TestTabConstructor:
#              РАЗДЕЛ "КОНСТРУКТОР"
# Проверяем активное состояние вкладок "Булки", "Соусы", "Начинки" в конструкторе


    # Проверяем активное состояние вкладоки "Булки"
    def test_constructor_sections_buns(self, driver):
        driver.get(url)
        # Проверяем "Булки", сначала переключаемся на "Соусы", чтобы сбросить активность с вкладки "Булки"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TAB_SAUCES)).click()
        # Ждём и кликаем по "Булки"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TAB_BUNS)).click()

        # Проверяем, что у вкладки есть активный класс
        tab_class = driver.find_element(*Locators.TAB_BUNS).get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in tab_class


    # Проверяем активное состояние вкладки "Соусы"
    def test_constructor_sections_sauces(self, driver):
        driver.get(url)

        # Ждём и кликаем по "Соусы"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TAB_SAUCES)).click()

        # Проверяем, что у вкладки есть активный класс
        tab_class = driver.find_element(*Locators.TAB_SAUCES).get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in tab_class


    # Проверяем активное состояние вкладки "Начинки"
    def test_constructor_sections_fillings(self, driver):
        driver.get(url)

        # Ждём и кликаем по "Начинки"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TAB_FILLINGS)).click()

        # Проверяем, что у вкладки есть активный класс
        tab_class = driver.find_element(*Locators.TAB_FILLINGS).get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in tab_class