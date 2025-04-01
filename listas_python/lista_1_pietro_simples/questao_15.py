#-*- coding: UTF-8 -*-
print('Olá, diga a temperatura que direi como está o clima')
temp = float(input('Digite a temperatura atual: '))
if temp <= 15:
    print('O clima está muito frio')
elif temp <= 23:
    print('O clima está frio')
elif temp <= 26:
    print('O clima está agradável')
elif temp <= 30:
    print('O clima está quente')
else:
    print('O clima está muito quente')
