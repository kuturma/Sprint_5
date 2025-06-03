from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    INPUT_NAME = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле "Имя"
    INPUT_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле "Email"
    INPUT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка зарегистрироваться
    ERROR_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')  # Ошибка пароля

    # Вход
    INPUT_LOGIN_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле логина
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']")  # Поле пароля
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка войти на странице авторизации
    LINK_LOGIN_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Главная кнопка входа
    LINK_LOGIN_HEADER = (By.LINK_TEXT, 'Личный Кабинет')  # Вход через "Личный кабинет"
    LINK_LOGIN_FROM_REGISTER = (By.LINK_TEXT, 'Войти')  # Вход через форму регистрации
    LINK_LOGIN_FROM_FORGOT = (By.LINK_TEXT, 'Войти')  # Вход через восстановление
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  #Оформить заказ

    # Личный кабинет
    LINK_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # Переход в личный кабинет
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Копка "Выход" в личном кабинете

    # Конструктор
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка "Конструктор"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип

    # Разделы конструктора
    TAB_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')  # Вкладка "Булки"
    TAB_SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')  # Вкладка "Соусы"
    TAB_FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')  # Вкладка "Начинки"