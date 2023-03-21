import math

def operation_put():
    op = input('(+, -, *, /)\nУкажите математическую операцию: ')
    while True:
        if op not in ('+', '-', '*', '/'):
            op = input('(+, -, *, /)\nНеобходимо ввести математическую опреацию: ')
        elif op in ('+', '-', '*', '/'):
            return op
        else:
            return True


def number_1(prev_result):
    while True:
        try:
            if prev_result == 0:
                a = float(input('Введите число: '))
            else:
                a = prev_result
            return a
        except ValueError:
            print('Error')
        
def number_2():
    while True:
        try:
            a = float(input('Введите число: '))
            return a
        except ValueError:
            print('Error')
     
def calc():
    print('Добро пожаловать в калькулятор\nЧтобы закончить работу нажмите комбинацию клавиш (Ctrl + C)')
    
    prev_result = 0

    while True:
        try:
            num_1 = number_1(prev_result)
            op = operation_put()
            num_2 = number_2()
        except KeyboardInterrupt:
            break
        
        try:
            result = choice(num_1, op, num_2)
            print(result)
        except ZeroDivisionError:
            continue

        prev_result = result

        #try:    
        #    extend = input('Продолжаем с полученным числом? (Y or another symbol)\n').upper()
        #    if extend == 'Y':
        #        prev_result = result
        #        continue
        #    else:
        #        prev_result = 0
        #        continue
        #except KeyboardInterrupt:
        #    break


def choice(num_1, op, num_2):
    if op == '+':
        return addition(num_1, num_2)

    if op == '-':
        return subscrition(num_1, num_2)

    if op == '*':
        return multiplication(num_1, num_2)

    if op == '/':
        return devision(num_1, num_2)

def addition(num_1, num_2):
    return num_1 + num_2

def subscrition(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def devision(num_1, num_2):
    return num_1 / num_2

    

if __name__ == '__main__':
    calc()
    

