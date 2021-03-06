# **********************************************************************************************************************
# Операции со строками
# Варианты оформления строк
text1 = 'Hello'
text2 = "World"

# Строки можно складывать
text3 = text1 + ', ' + text2 + '!'
print(text3)  # Hello, World!
print('***')

# Строки можно умножать
print(text3 * 3)  # Hello, World!Hello, World!Hello, World!
print('***')

# Со строкой можно работать как со списком символов
print(text3[0])  # H
print('***')

# Вариант форматирования строки
text4 = 'Hello{0}World{1}'.format(', ', '!')
print(text4)  # Hello, World!
print('***')

# Еще вариант форматирования строки
text4 = 'Hello{запятая_пробел}World{восклицательный_знак}'.format(запятая_пробел=', ', восклицательный_знак='!')
print(text4)  # Hello, World!
print('***')
# **********************************************************************************************************************
# Методы для строк
t = 'hello World'
# Копия строки написанная с заглавной буквы
print(t.capitalize())  # Hello world
# Копия строки где все буквы заменены на строчные
print(t.lower())  # hello world
# Копия строки где все буквы заменены на прописные
print(t.upper())  # HELLO WORLD
# Копия строки где прописные буквы заменены на заглавные, а заглавные на строчные
print(t.swapcase())  # HELLO wORLD
# Возвращает строку, где все элементы строки t объединены через строку в кавычках
print('--'.join(t))  # h--e--l--l--o-- --W--o--r--l--d
# Разбивает строку по делителю
for i in t.split(' '):
    print(i)
# Замена символов внутри строки
print(t.replace('l', '7'))  # he77o Wor7d
print('***')

# Возвращает True, если в строке хотя бы один символ и все символы строки являются буквами
print(t.isalpha())  # False
# Воаращает True, если в строке хотя бы один символ и все символы строки являются цифрами
print(t.isdigit())  # False
# и т.д.
# **********************************************************************************************************************
