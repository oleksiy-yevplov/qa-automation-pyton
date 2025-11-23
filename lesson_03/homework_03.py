# # alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# # task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# # task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# # Припустимо, alice_in_wonderland вже є
for char in alice_in_wonderland:
    if char == "'":
        print(char)

# # task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


# """
#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """
# # task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?
# """
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area+azov_sea_area
print( 'Чорне та Азовське моря разом займають площу', total_area,'км2')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total=375291
sklad_1_sklad_2=250449
sklad_2_sklad_3=222950
sklad_1=total-sklad_2_sklad_3
sklad_3=total-sklad_1_sklad_2
sklad_2=total-sklad_1-sklad_3
print('На кожному складі розміщена наступні кількість товарів:\n'
      'Склад №1:', sklad_1, 'товарів\n'
      'Склад №2:', sklad_2, 'товарів\n'
      'Склад №3:', sklad_3, 'товарів')


# task 06
"""
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
# """
shomisychnuy_platizg = 1179
kilkist_misychiv = 18
cost = shomisychnuy_platizg*kilkist_misychiv
print('Вартість комп’ютера складає',cost, 'гривень.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
# """
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print('Залишки від ділення:\n'
      'a)', a, '\n'
      'b)', b, '\n'
      'c)', c, '\n'
      'd)', d, '\n'
      'e)', e, '\n'
      'f)', f)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza=274
midl_pizza=218
juice=35
cake=350
water=21
total=4*large_pizza+2*midl_pizza+4*juice+cake+3*water
print('На замовлення Іринки потрібно всього', total, 'гривень.')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo=232
photo_on_page=8
total_pages=total_photo//photo_on_page
zalushok=total_photo%photo_on_page
if zalushok>0:
    total_pages=total_pages+1
print('Щоб вклеїти всі фото, Ігорю потрібно', total_pages, 'сторінок')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance=1600
petrol_consumption=9
capacity=48
petrol_consumption_1km=petrol_consumption/100
total_petrol=distance*petrol_consumption_1km
petrol_station_visit=int(total_petrol//capacity)
zalushok_petrol=total_petrol%capacity
if zalushok_petrol>0:
    petrol_station_visit=petrol_station_visit+1
print('Для подорожі знадобиться', total_petrol, 'літрів бензину')
print('Родині необхідно буде заїхати на заправку під час цієї подорожі', petrol_station_visit, 'рази')