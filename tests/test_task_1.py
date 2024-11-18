import unittest
from io import StringIO
from unittest.mock import patch

from src.task_1 import main


class TestMainFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    @patch("builtins.input", side_effect=["5", "3"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_numeric_input(self, mock_stdout, mock_input):
        main()
        self.assertIn("Результат: 8.0", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["abc", "xyz"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_string_input(self, mock_stdout, mock_input):
        main()
        self.assertIn("Результат: abcxyz", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["10.5", "2.5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_float_input(self, mock_stdout, mock_input):
        main()
        self.assertIn("Результат: 13.0", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["123", "abc"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_mixed_input(self, mock_stdout, mock_input):
        main()
        self.assertIn("Результат: 123abc", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        main()
        self.assertIn("Результат: ", mock_stdout.getvalue())  # Ожидается пустая строка
