#-*- coding: UTF-8 -*-
print('Olá, me de um número é primo ou não')
num = int(input('Digite o número: '))
def primo(num):
    for y in range(2,num):
        if num % y == 0:
            print('O número', num,'não é primo')
            break
        else:
            print('O número', num,'é primo')
primo(num)
