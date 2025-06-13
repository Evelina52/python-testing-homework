# Python Testing Homework

## Цель задания
Освоить основы тестирования в Python с использованием unittest и pytest.

## Описание файлов
- `test_with_unittest.py`: пример тестов с unittest
- `test_with_pytest.py`: пример тестов с pytest
- `calculate_average.py`: функция для вычисления среднего
- `average_unittest.py`: тесты для calculate_average с unittest
- `average_pytest.py`: тесты для calculate_average с pytest
- `answers.md`: ответы на теоретические вопросы

## Инструкция по запуску
1. Установите зависимости:
   ```bash
   pip install pytest

## Как запустить тесты
python -m unittest test_with_unittest.py
python -m unittest average_unittest.py
pytest test_with_pytest.py
pytest average_pytest.py