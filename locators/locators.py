from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  ## Поле "Имя"
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  ## Поле "Email"
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']")  ## Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  ## Кнопка зарегистрироваться
    ERROR_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")  ## Ошибка пароля

    # Вход
    INPUT_LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  ## Поле логина
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']")  ## Поле пароля
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")  ### Кнопка войти на странице авторизации
    LINK_LOGIN_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  ## Главная кнопка входа
    LINK_LOGIN_HEADER = (By.LINK_TEXT, 'Личный Кабинет')  ## Вход через "Личный кабинет"
    LINK_LOGIN_FROM_REGISTER = (By.LINK_TEXT, 'Войти')  ## Вход через форму регистрации
    LINK_LOGIN_FROM_FORGOT = (By.LINK_TEXT, 'Войти')  ## Вход через восстановление
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  ## Оформить заказ

    # Личный кабинет
    LINK_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # Переход в личный кабинет
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Копка "Выход" в личном кабинете

    # Конструктор
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка "Конструктор"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип

    # Разделы конструктора
    TAB_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]")  ## Вкладка "Булки"
    TAB_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")  ## Вкладка "Соусы"
    TAB_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]")  ## Вкладка "Начинки"