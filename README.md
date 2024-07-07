## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/StepanKazakov/diplom_1.git
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # В Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Запуск тестов с отчетом о покрытии

```sh
pytest --cov=praktikum --cov-report=html
```

## Подробности о тестах

### Тесты Bun

	•	test_bun_get_name - Тестирует метод get_name класса Bun.
	•	test_bun_get_price - Тестирует метод get_price класса Bun.

### Тесты Ingredient

	•	test_ingredient_get_name - Тестирует метод get_name класса Ingredient.
	•	test_ingredient_get_price - Тестирует метод get_price класса Ingredient.
	•	test_ingredient_get_type - Тестирует метод get_type класса Ingredient.

### Тесты Burger

	•	test_set_buns - Тестирует метод set_buns класса Burger.
	•	test_add_ingredient - Тестирует метод add_ingredient класса Burger.
	•	test_remove_ingredient - Тестирует метод remove_ingredient класса Burger.
	•	test_move_ingredient - Тестирует метод move_ingredient класса Burger.
	•	test_get_price - Тестирует метод get_price класса Burger.
	•	test_get_receipt - Тестирует метод get_receipt класса Burger.

### Тесты Database

	•	test_available_buns - Тестирует метод available_buns класса Database.
	•	test_available_ingredients - Тестирует метод available_ingredients класса Database.
