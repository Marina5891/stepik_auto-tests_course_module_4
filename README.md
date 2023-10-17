# Итоговое задание курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/lesson/201964/step/14?unit=176022)

## Структура проекта

- pages
  - base_page.py
  - basket_page.py
  - locators.py
  - login_page.py
  - main_page.py
  - product_page.py
- \_\_init\_\_.py
- conftest.py
- pytest.ini
- README.md
- requirements.txt
- test_main_page.py
- test_product_page.py

## Тесты для review

Тесты, которые необходимо проверить в итоговом задании помечены в коде маркировой **need_review**. Данные тесты находятся в файле [**test_product_page.py**](https://github.com/Marina5891/stepik_auto-tests_course_module_4/blob/main/test_product_page.py)

### Перечень тестов:

- test_user_can_add_product_to_basket
- test_guest_can_add_product_to_basket
- test_guest_cant_see_product_in_basket_opened_from_product_page
- test_guest_can_go_to_login_page_from_product_page

Запуск тестов выполняется командой `pytest -v --tb=line --language=en -m need_review`

## Окружение

Операционная система Linux Mint 21.2 Cinnamon  
Браузер Chrome, версия 117.0.5938.132 (Официальная сборка), (64 бит)  
Версия Python 3.10.12

Все скрипты запускались в виртуальном окружении.

Для работы в виртуальном окружении на компьютере должны быть установлены система управления пакетами **pip** и модуль **venv**.

Создание папки для виртуального окружения и переход в нее:

```
mkdir environment
cd environment
```

Создание виртуального окружения:
`python3 -m venv selenium_env`

Команда для запуска виртуального окружения:
`source selenium_env/bin/activate`

Версии пакетов, которые были использованы при написании проекта указаны в файле **requirements.txt**. Их установку можно выполнить командой:
`pip install -r requirements.txt`
_Обратите внимание, что установку пакетов нужно производить после запуска виртуального окружения и перехода в папку с проектом._

Команда для выхода из виртуального окружения:
`deactivate`
