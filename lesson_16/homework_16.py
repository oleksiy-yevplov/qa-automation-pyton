# Генератори:

# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    current = 0
    while current <= n:
        yield current
        current += 2
        
for num in even_numbers(10):
    print(num)


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
for num in fibonacci(30):
        print(num)

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  
    def __iter__(self):
        return self 

    def __next__(self):
        if self.index < 0:
            raise StopIteration  
        value = self.data[self.index]
        self.index -= 1 
        return value
my_list = [10, 20, 30, 40]
rev_iter = ReverseIterator(my_list)

for item in rev_iter:
    print(item)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, n):
        self.n = n            
        self.current = 0     

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.n:
            raise StopIteration 
        value = self.current
        self.current += 2       
        return value
evens = EvenIterator(10)
for num in evens:
    print(num)

# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs) 
        print(f"Результат: {result}")
        return result
    return wrapper
@logger
def add(a, b):
    return a + b

@logger
def greet(name="QA"):
    return f"Привіт, {name}!"
add(10, 5)
greet(name="Олeксій")

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    """
    Декоратор, який перехоплює винятки під час виконання функції
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Виняток у функції {func.__name__}: {e}")
            return None  
    return wrapper
@exception_handler
def add(a, b):
    return a + b

@exception_handler
def greet(name="QA"):
    return f"Привіт, {name}!"
