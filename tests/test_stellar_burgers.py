import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data_generate import generate_email, generate_name, generate_password


class TestStellarBurgers:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

#              РЕГИСТРАЦИЯ

# Проверяем успешную регистрацию с помощью генератора случайных данных
    def test_successful_registration(self, driver):
        driver.get(f"{self.BASE_URL}/register")
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
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.INPUT_LOGIN_EMAIL))


    # Проверяем регистрацию с коротким паролем
    def test_registration_with_short_password(self, driver):
        driver.get(f"{self.BASE_URL}/register")
        name = generate_name()
        email = generate_email()
        password = "123"

        # Заполняем форму регистрации через поиск элементов на странице регистрации
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

        # Нажимаем кнопку регистрации
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждём появления ошибки
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD))


#               ВХОД

# Проверяем успешный вход в систему из различных страниц сайта
# Создаём параметризацю для входа из различных страниц сайта
    @pytest.mark.parametrize("path", [
        "", # Главная страница
        "login", # Страница входа (личный кабинет)
        "register", # Страница регистрации
        "forgot-password" # Страница восстановления пароля
        ])
    def test_login_from_various_paths(self, driver, path):
        email = "kuturmin@mail.ru"  # Используем существующую почту
        password = "kuturmin"       # Существующий пароль
        
        # Переход на страницы через указанные пути
        driver.get(f"{self.BASE_URL}/{path}")

        # Переходим на страницу входа через главную страницу
        if path == "":
            driver.find_element(*Locators.LINK_LOGIN_MAIN).click()
        # Переходим на страницу входа через страницу регистрации
        elif path == "register":
            driver.find_element(*Locators.LINK_LOGIN_FROM_REGISTER).click()
        # Переходим на страницу входа через страницу восстановления пароля
        elif path == "forgot-password":
            driver.find_element(*Locators.LINK_LOGIN_FROM_FORGOT).click()

        # Заполняем форму входа используя явное ожидание
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_EMAIL)).send_keys(email)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_LOGIN_PASSWORD)).send_keys(password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()

        # Проверяем наличие кнопки "Оформить заказ" после входа
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


#         ПЕРЕХОД В ЛИЧНЫЙ КАБИНЕТ

# Проверяем переход в личный кабинет по кнопке в шапке сайта "Личный кабинет"
    def test_go_to_personal_account(self, driver):
        driver.get(self.BASE_URL)

        # Ждём и кликаем по кнопке "Личный кабинет" в шапке сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN_HEADER)).click()
        
        #Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys("kuturmin@mail.ru")
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys("kuturmin")

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Проверяем, что появилась кнопка "Выйти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGOUT))


#            ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР

# Проверяем переход из личного кабинета в конструктор по кнопке "Конструктор" и логотипу сайта
# Создаём параметризацю для перехода по разным элементам на странице из личного кабинета
    @pytest.mark.parametrize("element", [Locators.LINK_CONSTRUCTOR, Locators.LOGO])
    def test_return_to_constructor(self, driver, element):
        driver.get(self.BASE_URL)

        # Кликаем по кнопке "Личный кабинет" в шапке сайта
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys("kuturmin@mail.ru")
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys("kuturmin")

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждём и кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по нужному элементу (логотип или "Конструктор")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element)).click()

        # Проверяем, что перешли на главную
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{self.BASE_URL}/"))
        assert driver.current_url == f"{self.BASE_URL}/"


#               ВЫХОД ИЗ АККАУНТА
    def test_logout(self, driver):
        driver.get(self.BASE_URL)

        # Переходим в авторизацию через кнопку в шапке сайта "Личный кабинет"
        driver.find_element(*Locators.LINK_LOGIN_HEADER).click()

        # Заполняем форму входа через поиск элементов на странице авторизации
        driver.find_element(*Locators.INPUT_LOGIN_EMAIL).send_keys("kuturmin@mail.ru")
        driver.find_element(*Locators.INPUT_LOGIN_PASSWORD).send_keys("kuturmin")

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Переходим в личный кабинет через кнопку "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACCOUNT)).click()

        # Ждём и кликаем по "Выйти"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)).click()

        # Проверяем, что появилась кнопка "Войти" на экране
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGIN))


#              РАЗДЕЛ "КОНСТРУКТОР"

# Проверяем активное состояние вкладок "Булки", "Соусы", "Начинки" в конструкторе
# Создаём параметризацю для проверки всех вкладок в конструкторе
    @pytest.mark.parametrize("tab_locator", [
        Locators.TAB_BUNS,
        Locators.TAB_SAUCES,
        Locators.TAB_FILLINGS
    ])
    def test_constructor_sections(self, driver, tab_locator):
        driver.get(self.BASE_URL)

        # Если проверяем "Булки", то сначала переключаемся на "Соусы", чтобы сбросить активность
        if tab_locator == Locators.TAB_BUNS:
            # Ждем и кликаем по "Соусы", чтобы сбросить активность
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TAB_SAUCES)).click()
            # Ждём и кликаем по "Булки"
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator)).click()
        else:
            # Ждём и кликаем по нужной вкладке (Соусы или Начинки)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator)).click()

        # Проверяем, что у вкладки есть активный класс
        tab_class = driver.find_element(*tab_locator).get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in tab_class, f"Вкладка не активна: {tab_class}"
