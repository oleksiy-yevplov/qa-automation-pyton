# 1. Homework 11
import unittest
from homeworks import sum_numbers


class TestSumNumbers(unittest.TestCase):

    def test_sum_numbers_positive(self):
        result = sum_numbers("1,2,3,4")
        self.assertEqual(result, 10)

    def test_sum_numbers_negative(self):
        result = sum_numbers("qwerty1,2,3")
        self.assertEqual(result, "Виникла помилка")

# 2. Homework 09

from homeworks import Triangle

class TestTriangleInit(unittest.TestCase):

    def test_triangle_init_positive(self):
        triangle = Triangle(10, 60)

        self.assertEqual(triangle.side, 10)
        self.assertEqual(triangle.alpha, 60)
        self.assertEqual(triangle.beta, 120)

    def test_triangle_init_negative(self):
        triangle = Triangle(-5, 200)

        self.assertFalse(hasattr(triangle, "side"))
        self.assertFalse(hasattr(triangle, "alpha"))
        self.assertFalse(hasattr(triangle, "beta"))


# 3. Homework 07.1
from homeworks import multiplication_table

class TestMultiplicationTable(unittest.TestCase):

    def test_multiplication_table_positive(self):
        result = multiplication_table(5)
        self.assertIn("5x1=5", result)

    def test_multiplication_table_negative(self):
        result = multiplication_table(0)
        self.assertEqual(result, [])

# 4. Homework 07.2
from homeworks import sum_two_num

class TestSumTwoNum(unittest.TestCase):

    def test_sum_two_num_positive(self):
        result = sum_two_num(5, 7)
        self.assertEqual(result, 12)

    def test_sum_two_num_negative(self):
        with self.assertRaises(TypeError):
            sum_two_num("5", 7)

# 5. Homework 07.3
from homeworks import average

class TestAverage(unittest.TestCase):

    def test_average_positive(self):
        result = average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_average_negative(self):
        result = average([])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
