# 1. Homework 11
def sum_numbers(value):
    try:
        numbers = value.split(",")
        total = 0
        for num in numbers:
            total += int(num)
        return total
    except ValueError:
        return "Виникла помилка"

# 2. Homework 09
class Triangle:
    def __init__(self, side, alpha):
        if side > 0:
            self.side = side
        else:
            pass

        if 0 < alpha < 180:
            self.alpha = alpha
            self.beta = 180 - alpha
        else:
            pass

# 3. Homework 07.1
def multiplication_table(number):
    if number <= 0:
        return []
    multiplier = 1
    result_list = []
    while number * multiplier <= 25:
        result = f"{number}x{multiplier}={number*multiplier}"
        result_list.append(result)
        multiplier += 1
    return result_list

# 4. Homework 07.2
def sum_two_num(a,b):
    return a+b

# 5. Homework 07.3
def average(numbers):
    if len(numbers) == 0:   
        return 0
    return sum(numbers) / len(numbers)
