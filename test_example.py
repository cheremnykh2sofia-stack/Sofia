"""
Тестовый файл для проекта Sofia
"""

import unittest


class TestExample(unittest.TestCase):
    """Пример тестового класса"""

    def test_addition(self):
        """Тест сложения"""
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        """Тест вычитания"""
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        """Тест умножения"""
        self.assertEqual(3 * 4, 12)

    def test_string_operations(self):
        """Тест операций со строками"""
        text = "Sofia"
        self.assertEqual(text.lower(), "sofia")
        self.assertEqual(len(text), 5)
        self.assertTrue(text.startswith("S"))


if __name__ == '__main__':
    unittest.main()
