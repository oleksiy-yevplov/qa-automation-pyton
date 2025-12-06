user_text=input("Введіть текст для перевірки:")
input_text=set(user_text)
if len(input_text)>10:
  print(True)
else:
  print(False)