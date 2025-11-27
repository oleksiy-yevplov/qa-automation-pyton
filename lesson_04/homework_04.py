adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. And while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but .... remained to whitewash. .... By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""
normal_text = adwentures_of_tom_sawer.replace("\n", " ")
print(normal_text)
# task 02 ==
""" Замініть .... на пробіл
"""
normal_text_1= (normal_text.replace("...."," "))
print(normal_text_1)
print
# # task 03 ==
# """ Зробіть так, щоб у тексті було не більше одного пробілу між словами.
# """
normal_text_2 = " ".join(
    normal_text.replace("....", " ").split()
)

print(normal_text_2)


# # task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h"
# """
print (normal_text_2.count("h"))

# # task 05
# """ Виведіть, скільки слів у тексті починається з Великої літери?
# """
print(sum(word[0].isupper() for word in normal_text_2.split()))


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

word_tom = normal_text_2.split()
print(word_tom.index("Tom", word_tom.index("Tom") + 1))

# # task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences
# """

import re 
adwentures_of_tom_sawer_7 = adwentures_of_tom_sawer.replace("....", " ") 
print ("task02:", adwentures_of_tom_sawer_7) 
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', adwentures_of_tom_sawer_7) 
adwentures_of_tom_sawer_sentences = [sentence.replace("\n", " ") for sentence in adwentures_of_tom_sawer_sentences] 
print(adwentures_of_tom_sawer_sentences)


# task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
# """

fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False 
for sentence in adwentures_of_tom_sawer_sentences: 
    if sentence.strip().startswith("By the time"): 
        found = True 
        break 
if found: 
    print("Є таке речення, яке починається з 'By the time'.") 
else: 
    print("Немає речень, які починаються з 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(word_count)
