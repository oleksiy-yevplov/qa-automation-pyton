import pytest
import allure

from lesson_24.homeworks import sum_numbers
from lesson_24.homeworks import Triangle
from lesson_24.homeworks import multiplication_table
from lesson_24.homeworks import sum_two_num
from lesson_24.homeworks import average


@allure.feature("Homework 11 - Sum numbers")
def test_sum_numbers_positive():
    with allure.step("Виконуємо сумування чисел"):
        result = sum_numbers("1,2,3,4")

    with allure.step("Перевіряємо результат"):
        assert result == 9


@allure.feature("Homework 11 - Sum numbers")
def test_sum_numbers_negative():
    with allure.step("Передаємо рядок"):
        result = sum_numbers("qwerty1,2,3")

    with allure.step("Перевіряємо повідомлення про помилку"):
        assert result == "Виникла помилка"


@allure.feature("Homework 09 - Triangle")
def test_triangle_init_positive():
    with allure.step("Створюємо трикутник"):
        triangle = Triangle(10, 60)

    with allure.step("Перевіряємо сторони та кути"):
        assert triangle.side == 10
        assert triangle.alpha == 60
        assert triangle.beta == 120


@allure.feature("Homework 09 - Triangle")
def test_triangle_init_negative():
    with allure.step("Створюємо невалідний трикутник"):
        triangle = Triangle(-5, 200)

    with allure.step("Перевіряємо що атрибути не створені"):
        assert not hasattr(triangle, "side")
        assert not hasattr(triangle, "alpha")
        assert not hasattr(triangle, "beta")


@allure.feature("Homework 07.1 - Multiplication table")
def test_multiplication_table_positive():
    with allure.step("Генеруємо таблицю множення"):
        result = multiplication_table(5)

    with allure.step("Перевіряємо результат"):
        assert "5x1=5" in result


@allure.feature("Homework 07.1 - Multiplication table")
def test_multiplication_table_negative():
    with allure.step("Передаємо нуль"):
        result = multiplication_table(0)

    with allure.step("Перевіряємо що список порожній"):
        assert result == []


@allure.feature("Homework 07.2 - Sum two numbers")
def test_sum_two_num_positive():
    with allure.step("Складаємо два числа"):
        result = sum_two_num(5, 7)

    with allure.step("Перевіряємо результат"):
        assert result == 11


@allure.feature("Homework 07.2 - Sum two numbers")
def test_sum_two_num_negative():
    with allure.step("Передаємо невалідний тип"):
        with pytest.raises(TypeError):
            sum_two_num("5", 7)


@allure.feature("Homework 07.3 - Average")
def test_average_positive():
    with allure.step("Рахуємо середнє значення"):
        result = average([1, 2, 3, 4, 5])

    with allure.step("Перевіряємо результат"):
        assert result == 3.0


@allure.feature("Homework 07.3 - Average")
def test_average_negative():
    with allure.step("Передаємо пустий список"):
        result = average([])

    with allure.step("Перевіряємо що результат 0"):
        assert result == 0