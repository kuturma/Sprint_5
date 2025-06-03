import random
import string


def generate_name() -> str:
    """Генерируем случайное имя"""
    name_length = random.randint(3, 6)
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
    return name
    
 
def generate_email() -> str:
    """Генерируем email в формате anton_kuturmin_23_XXX@domains"""
    # Генерируем 3 случайные цифры
    random_digits = ''.join(random.choices(string.digits, k=3))
    domains = ['gmail.com', 'ya.ru', 'mail.ru', 'yandex.ru']
    return f'anton_kuturmin_23_{random_digits}@{random.choice(domains)}'.lower()
    
 
def generate_password(min_lenght=6, max_leght=12) -> str:
    """Генерируем случайный пароль"""
    password_length = random.randint(min_lenght, max_leght)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=password_length))
    return password