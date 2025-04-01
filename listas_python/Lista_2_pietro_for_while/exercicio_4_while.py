#-*- coding: UTF-8 -*-
print('Olá, diga os números inteiros que direi a soma dos pares e dos ímpares')
par = 0
impar = 0
while True:
    num = int(input('Digite o valor: '))
    if num > 1000:
        break
    elif num % 2 == 0:
        par = par + num
    elif num % 2 != 0:
        impar = impar + num
print(f'A soma dos números pare é {par} e a soma dos númreos impares é {impar}')
        
