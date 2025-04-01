#-*- coding: UTF-8 -*-
print('Diga o valor do produto, que direi o valor para venda')
pro = float(input('Diga o valor do produto: '))
if pro < 20:
    val = (pro*45) / 100
    val1 = pro + val
    print('O valor de venda é: ', val1)
elif pro >= 20:
    va2 = (pro*30) / 100
    val3 = pro + va2
    print('O valor de venda é: ', val3)
