import random
import string

# Генерируем случайное имя
def generate_name() -> str:
    name_length = random.randint(3, 6)
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
    return name
    
# Генерируем email в формате anton_kuturmin_23_XXX@domains
def generate_email() -> str:
    # Генерируем 3 случайные цифры
    random_digits = ''.join(random.choices(string.digits, k=3))
    domains = ['gmail.com', 'ya.ru', 'mail.ru', 'yandex.ru']
    return f'anton_kuturmin_23_{random_digits}@{random.choice(domains)}'.lower()
    
# Генерируем случайный пароль
def generate_password(min_lenght=6, max_lenght=12) -> str:
    """Генерируем случайный пароль"""
    password_length = random.randint(min_lenght, max_lenght)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=password_length))
    return password

# Генерируем короткий пароль (от 1 до 3 символов)
def generate_short_password(min_lenght=1, max_lenght=3) -> str:
    password_length = random.randint(min_lenght, max_lenght)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=password_length))
    return password

#Храним вводимые данные пользователя заранее зарегистрированные
class UserData:

    email = "kuturmin@mail.ru"
    password = "kuturmin"
    
   