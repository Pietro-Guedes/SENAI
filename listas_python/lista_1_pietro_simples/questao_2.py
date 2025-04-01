#-*- coding: UTF-8 -*-
import math
print('Digite um número que eu direi a riaz quadrada dele.')
num = int(input('Digite o número: '))
if num >= 0:
    raiz = math.sqrt(num)
    print('A raiz do número é: ', raiz)
else:
    potencia = num**2
    print('O número é: ', potencia)
