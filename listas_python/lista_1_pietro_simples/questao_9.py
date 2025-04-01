#-*- coding: UTF-8 -*-
print('Diga seu peso e altura que direi cê é favorável')
peso = float(input('Diga seu peso: '))
alt = float(input('Diga sua altura: '))
alt2 = alt * 2
resul = peso // alt2
if resul < 20:
    print('Você está abaixo do peso')
elif resul < 25:
    print('Você está com o peso normal')
elif resul < 30:
    print('Você está sobre peso')
elif resul < 40:
    print('Você está obeso')
elif resul >=40:
    print('Você está obeso mórbido')
