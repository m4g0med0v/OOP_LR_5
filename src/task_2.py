#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу:
# Напишите программу, которая будет генерировать матрицу из случайных целых
# чисел. Пользователь может указать число строк и столбцов, а также диапазон
# целых чисел. Произведите обработку ошибок ввода пользователя.


import random


def generate_matrix(
    rows: int, cols: int, min_val: int, max_val: int
) -> list[list[int]]:
    """
    Генерирует матрицу заданного размера,
    заполненную случайными целыми числами.
    """
    return [
        [random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)
    ]


def main() -> None:
    try:
        rows = int(input("Введите число строк: "))
        cols = int(input("Введите число столбцов: "))
        min_val = int(input("Введите минимальное значение: "))
        max_val = int(input("Введите максимальное значение: "))

        if rows <= 0 or cols <= 0:
            raise ValueError("Число строк и столбцов должно быть больше нуля.")
        if min_val > max_val:
            raise ValueError("Минимальное значение не может быть больше максимального.")

        matrix = generate_matrix(rows, cols, min_val, max_val)

        print("\nСгенерированная матрица:")
        for row in matrix:
            print(" ".join(map(str, row)))

    except ValueError as e:
        print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
