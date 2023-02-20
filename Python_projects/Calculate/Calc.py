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


def first():
    while True:
        try:
            a = float(input('Введите первое число: '))
            return a
        except ValueError:
            print('Error')
        continue


def second():
    while True:
        try:
            a = float(input('Введите второе число: '))
            return a
        except ValueError:
            print('Error')
        continue

     
def calc():

    while True:
        n = ''
        num_1 = first()
        oper = operation_put()
        num_2 = second()

        for i in oper:

            n += i[0]

            if n == '+':
                print(num_1 + num_2)

            elif n == '-':
                print(num_1 - num_2)

            elif n == '*':
                print(num_1 * num_2)

            elif n == '/':
                if num_2 == 0:
                    print('Деление на ноль не имеет смысла. Число стремится к бесконечности')
                    break
                print(num_1 / num_2)
                

calc()
    

