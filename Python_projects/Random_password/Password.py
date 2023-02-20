import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

def count_pass():
    while True:
        count = input('Введите количество паролей: ')
        if not count.isdigit() or int(count) < 1:
            print('Нужно ввести число больше 0!')
            continue
        return int(count)

def lenght_pass():
    while True:
        lenght = input('Введи количество символов: ')
        if not lenght.isdigit() or 8 > int(lenght) or int(lenght) > 36:
            print('Нужно ввести число от 8 до 36!')
            continue
        return int(lenght)

def need_or_not():
    while True: 
        a = input('Введите y или n: ').lower()
        if a != 'y' and a != 'n':
            print('Нужно ввести "y" или "n" !')
        elif a == 'y':
            return True 
        elif a == 'n':
            return False

print('Сколько паролей сгенерировать?')
count_pass = count_pass()

print('Какая длина одного пароля? (от 8 до 36)')
lenght_pass = lenght_pass()

print('Включать ли цифры 0123456789? (Yes = y, No = n)')
if need_or_not():
    chars  += digits
    
print('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (Yes = y, No = n)')
if need_or_not():
    chars += lowercase_letters
    
print('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? (Yes = y, No = n)')
if need_or_not():
    chars+= uppercase_letters
    
print('Включать ли символы "!#$%&*+-=?@^_"? (Yes = y, No = n)')
if need_or_not():
    chars+= punctuation

print('Исключать ли неоднозначные символы "il1Lo0O"? (Yes = y, No = n)')
if need_or_not():
    for i in 'il1Lo0O': 
        chars = chars.replace(i, '')

def generate_password():
    password = ''
    for _ in range(lenght_pass):
         password += random.choice(chars)
    return password


for _ in range(count_pass):
 print('Сгенерированный пароль: ', generate_password())
    
