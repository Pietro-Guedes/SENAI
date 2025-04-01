#-*- coding: UTF-8 -*-
print('Olá, me de o número que irei fazer a contagem regressiva para o ano novo')
num = int(input('Digite o número: '))
def contagem(num):
    for y in range(num, -1, -1):
        print(y)
contagem(num)
print('Feliz ano novo')
