user_text=""
while "h" not in user_text:
  user_text=input("Введіть текст для перевірки наявності літери 'h':")
  if "h" not in user_text.lower():
    continue
  else:
    print("Ви ввели літеру'h'")
    break

