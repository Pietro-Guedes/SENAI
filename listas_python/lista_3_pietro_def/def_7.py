#-*- coding: UTF-8 -*-
print('Olá, peça para fazer um cálculo de adição, subtração, multiplicação ou divisão que irie fazer')
num = int(input('Digite o número: '))
num2 = int(input('Digite o segundo número: '))
var = input('Digite qual operação usar: ')
def operacao():
    global num, num2, var
    if var == '+':
        num3 = num + num2
        print(f'O resultado é {num3}')
    elif var == '-':
        num4 = num - num2
        print(f'O reseltado é {num4}')
    elif var == '*':
        num5 = num * num2
        print(f'O resultado é {num5}')
    elif var == '/':
        num6 = num / num2
        print('O resultado é {num6}')
    else:
        print('Erro')
operacao()
