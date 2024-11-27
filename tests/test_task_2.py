import sys
from io import StringIO

import pytest

from src.task_2 import generate_matrix, main


class TestMainFunction:
    def test_generate_matrix(
        self,
    ):
        # Проверяем корректную генерацию матрицы
        rows, cols, min_val, max_val = 3, 4, 1, 10
        matrix = generate_matrix(rows, cols, min_val, max_val)
        # Проверяем количество строк
        assert len(matrix) == rows
        # Проверяем количество столбцов
        assert all(len(row) == cols for row in matrix)
        # Диапазон
        assert all(
            min_val <= value <= max_val for row in matrix for value in row
        )

    @pytest.mark.parametrize(
        "user_input, expected_output",
        [
            ("3\n4\n1\n10\n", "Сгенерированная матрица:"),
            (
                "0\n4\n1\n10\n",
                "Число строк и столбцов должно быть больше нуля.",
            ),
            (
                "3\n4\n10\n1\n",
                "Минимальное значение не может быть больше максимального.",
            ),
            ("a\n4\n1\n10\n", "Ошибка ввода"),
        ],
    )
    def test_main(self, user_input, expected_output):
        # Подмена ввода и вывода
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        try:
            sys.stdin = StringIO(user_input)
            output = StringIO()
            sys.stdout = output
            main()
            result = output.getvalue()
            assert expected_output in result
        finally:
            sys.stdin = original_stdin
            sys.stdout = original_stdout
