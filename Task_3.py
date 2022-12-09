# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# вариант 1:
# txt = input("Введите текст: ")
# find = "абв"
# result = txt.split(' ')
#
# for words in result:
#     if find not in words:
#         print(words, end=' ')

# вариант 2:

txt = input("Введите текст: ")
result = txt.split(' ')
new_list = list(filter(lambda item: 'абв' not in item, result))
print(new_list)