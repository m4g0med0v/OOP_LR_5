#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу:
# Напишите программу, которая запрашивает ввод двух значений.


def main() -> None:
    value1: str = input("Первое значение: ")
    value2: str = input("Второе значение: ")

    try:
        # Попробуем преобразовать значения в числа
        num1: float = float(value1)
        num2: float = float(value2)
        num_result: float = num1 + num2
        print(f"Результат: {num_result}")
    except ValueError:
        # Если преобразование не удалось, работаем как со строками
        str_result: str = value1 + value2
        print(f"Результат: {str_result}")


if __name__ == "__main__":
    main()
