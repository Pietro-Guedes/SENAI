#-*- coding: UTF-8 -*-
print('Olá, diga dois números inteiros que direi cê o primeiro é dividido pelo segundo')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
total = a % b
if total != 0:
    print('O primeiro número não é divisivel pelo segundo')
else:
    print('O número primeiro número é divisivel pelo segundo')
