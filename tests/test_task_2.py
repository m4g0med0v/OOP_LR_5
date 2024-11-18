import unittest
from io import StringIO
from unittest.mock import patch

from src.task_2 import generate_matrix, main


class TestMatrixGeneration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    def test_generate_matrix(self):
        # Проверяем корректную генерацию матрицы
        rows, cols, min_val, max_val = 3, 4, 1, 10
        matrix = generate_matrix(rows, cols, min_val, max_val)
        self.assertEqual(len(matrix), rows)  # Проверяем количество строк
        self.assertTrue(
            all(len(row) == cols for row in matrix)
        )  # Проверяем количество столбцов
        self.assertTrue(
            all(min_val <= value <= max_val for row in matrix for value in row)
        )  # Проверяем диапазон значений

    @patch("builtins.input", side_effect=["3", "4", "1", "10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Сгенерированная матрица:", output)

    @patch("builtins.input", side_effect=["0", "4", "1", "10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_invalid_rows(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка ввода", output)
        self.assertIn("Число строк и столбцов должно быть больше нуля.", output)

    @patch("builtins.input", side_effect=["3", "4", "10", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_min_greater_than_max(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка ввода", output)
        self.assertIn(
            "Минимальное значение не может быть больше максимального.", output
        )

    @patch("builtins.input", side_effect=["a", "4", "1", "10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_non_integer_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка ввода", output)
