# Автоматизированное тестирование Stellar Burgers

Проект для автоматизации тестирования веб-приложения Stellar Burgers с использованием Selenium WebDriver, pytest и Python.

## Описание

Данный проект включает автотесты для веб-сайта Stellar Burgers, который предоставляет конструктор бургеров и возможность регистрации пользователей. Тесты покрывают следующие функциональные аспекты:
- Регистрация нового пользователя.
- Вход в аккаунт через разные формы (главная страница, форма восстановления пароля и т.д.).
- Проверка работы личного кабинета и конструктора.
- Проверка выхода из аккаунта.

В проекте используется pytest для запуска тестов и Selenium WebDriver для автоматизации действий в браузере.

## Структура проекта

<pre>Sprint_5/
├── conftest.py
├── data.py                   
├── helpers.py                
├── locators.py                
├── tests/                     
│   ├── test_login.py   
│   ├── test_logout.py
│   ├── test_registration.py 
│   ├── test_navigation_to_personal_account.py 
│   ├── test_navigation_to_constructor.py
│   └── test_constructor_section.py    
└── .gitignore</pre>

## Технологии

- Python 3.13.3
- Selenium WebDriver для взаимодействия с браузером.
- pytest для выполнения и организации тестов.
- webdriver-manager для автоматической установки и управления драйверами.

## Как установить проект

### 1. Клонируйте репозиторий:
```git clone <URL репозитория>```
### 2. Создайте и активируйте виртуальное окружение:
- Windows
```python -m venv venv```
```venv\Scripts\activate```
- MacOS/Linux
```source venv/bin/activate```
### 3. Установите зависимости:
   ```pip install pytest ```
   ```pip install selenium```

## Запуск проекта

- Для запуска тестов используйте команду pytest:
```pytest -v```