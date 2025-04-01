#-*- coding: UTF-8 -*-
print('Olá, diga um número que mostrarei o fatorial dele')
fat = 1
num = int(input('Digite o número: '))
for x in range(1,num+1):
    fat = fat * x
print(f'O fatorial de {num} é {fat}')
