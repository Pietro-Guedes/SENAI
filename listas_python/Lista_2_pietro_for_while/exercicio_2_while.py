#-*- coding: UTF-8 -*-
print('Olá, diga os números que eu direi qual o maior e o menor')
num = float(input('Digite o número: '))
maior = num
menor = num
while True:
    num = float(input('Digite o número: ' ))
    if num < 0:
        break
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'O maior valor digitado é {maior} e o menor é {menor}')
    
