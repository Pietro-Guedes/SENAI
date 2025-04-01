#-*- coding: UTF-8 -*-
print('Olá, digite o número que direi a tabuada dele')
num = int(input('Digite o número: '))
def tabuada(num):
    for y in range(1, 11):
        print(num, 'x', y, '=', num * y)
tabuada(num)
