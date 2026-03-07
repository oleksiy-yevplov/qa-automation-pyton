import pytest

from lesson_23.homeworks import sum_numbers
from lesson_23.homeworks import Triangle
from lesson_23.homeworks import multiplication_table
from lesson_23.homeworks import sum_two_num
from lesson_23.homeworks import average

# 1. Homework 11
def test_sum_numbers_positive():
    result = sum_numbers("1,2,3,4")
    assert result == 10


def test_sum_numbers_negative():
    result = sum_numbers("qwerty1,2,3")
    assert result == "Виникла помилка"


# 2. Homework 09
def test_triangle_init_positive():
    triangle = Triangle(10, 60)

    assert triangle.side == 10
    assert triangle.alpha == 60
    assert triangle.beta == 120


def test_triangle_init_negative():
    triangle = Triangle(-5, 200)

    assert not hasattr(triangle, "side")
    assert not hasattr(triangle, "alpha")
    assert not hasattr(triangle, "beta")


# 3. Homework 07.1
def test_multiplication_table_positive():
    result = multiplication_table(5)
    assert "5x1=5" in result


def test_multiplication_table_negative():
    result = multiplication_table(0)
    assert result == []


# 4. Homework 07.2
def test_sum_two_num_positive():
    result = sum_two_num(5, 7)
    assert result == 12


def test_sum_two_num_negative():
    with pytest.raises(TypeError):
        sum_two_num("5", 7)


# 5. Homework 07.3
def test_average_positive():
    result = average([1, 2, 3, 4, 5])
    assert result == 3.0


def test_average_negative():
    result = average([])
    assert result == 0