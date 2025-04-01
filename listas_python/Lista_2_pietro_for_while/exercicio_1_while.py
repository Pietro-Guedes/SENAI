#-*- coding: UTF-8 -*-
print('Olá, diga os números a seguir, que direi a soma e a média deles, para finalzar digite negativo')
x = 0
soma = 0
while True:
    num = int(input('Digite o valor: '))
    if num < 0:
        break
    soma += 1
    x += num
print(f'A média dos valores é {x/soma} e a soma é {x}')
     
