#-*- coding: UTF-8 -*-
print('Olá, digite o número inteiro que direi cê é múltiplo de 3')
num = int(input('Digite o número: '))
total = num % 3
if total != 0:
    print('O número não é múltiplo de 3')
else:
    print('O número é múltiplo de 3')
