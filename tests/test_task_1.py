import sys
from io import StringIO

import pytest

from src.task_1 import main


class TestMainFunction:
    @pytest.mark.parametrize(
        "user_input, expected_output",
        [
            ("5\n3\n", "Результат: 8.0"),
            ("abc\nxyz\n", "Результат: abcxyz"),
            ("10.5\n2.5\n", "Результат: 13.0"),
            ("123\nabc\n", "Результат: 123abc"),
            ("\n\n", "Результат: "),
        ],
    )
    def test_main_function_no_mock(self, user_input, expected_output):
        # Подмена стандартного ввода и вывода
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
            # Восстановление стандартного ввода и вывода
            sys.stdin = original_stdin
            sys.stdout = original_stdout
