import random
import string

BASE_URL = "https://stellarburgers.nomoreparties.site"

FIRST_NAME = "Anastasia"
LAST_NAME = "Prodan"
COHORT_NUMBER = "22"
DOMAIN = "yandex.ru"

def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def generate_unique_email():
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{FIRST_NAME.lower()}{LAST_NAME.lower()}{COHORT_NUMBER}{random_digits}@{DOMAIN}"
    return email

def generate_random_password():
    return generate_random_string(length=8)

# Уникальный пользователь для регистрации в рантайме
TEST_USER = {
    "name": FIRST_NAME,
    "email": generate_unique_email(),
    "password": generate_random_password()
}

# Зарегистрированный заранее пользователь
EXISTING_USER = {
    "name": FIRST_NAME,
    "email": "anastasiaprodan22@yandex.ru",
    "password": "ya10052025"
}

# Невалидный пользователь
INVALID_USER = {
    "name": FIRST_NAME,
    "email": "invalid_email@yandex.ru",
    "password": "short"
}