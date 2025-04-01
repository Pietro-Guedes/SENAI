#-*- coding: UTF-8 -*-
print('Olá, direi os divisores de um número')
num = int(input('Digite o número: '))
for x in range(1,num+1):
    if num % x == 0:
        print(x)
