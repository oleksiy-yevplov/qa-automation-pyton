# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number*multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
       # if  result > 25:
            # Enter the action to take if the result is greater than 25
        #    pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(a,b):
    return a+b
result=sum_two_num (5,7)
print("Сума чисел складає:", result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:   
        return 0
    return sum(numbers) / len(numbers)
nums = [1, 2, 3, 4, 5]
result = average(nums)
print("Середнє арифметичне:", result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello World"))  
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    longest = words[0]  
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

words_list = ["apple", "banana", "cherry", "strawberry"]
result = longest_word(words_list)
print("Найдовше слово:", result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  
str1 = "Hello, world!"
str2 = "cat"
print(find_substring(str1, str2))  


# task 7
# Моя домашка 6.4
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
lst = [1,2,3,4,5,6,8,56,78,99,3,5,6,78,99,34,34,66,7,88]
result = sum_even_numbers(lst)
print("Сума парних чисел:", result)
# task 8
# Моя домашка 6.3
def filter_strings(lst):
    result = []
    for element in lst:
        if isinstance(element, str):
            result.append(element)
    return result
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)
print(lst2)
# task 9
# Моя домашка 6.2
def wait_for_h():
    while True:
        user_text = input("Введіть текст для перевірки наявності літери 'h': ")
        if "h" in user_text.lower():
            print("Ви ввели літеру 'h'")
            return user_text  
   
entered_text = wait_for_h()
print("Текст, який містить 'h':", entered_text)

# task 10
#Задача з першої домашки
def total_book_price(book_1_price):
    book_2 = book_1_price + 2
    book_3 = (book_1_price + book_2) / 2
    total = book_1_price + book_2 + book_3
    return total
book_1 = 8
total = total_book_price(book_1)
print("Якщо купити по одному примірнику кожної книги, то вони будуть коштувати", total, "грн.")


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""