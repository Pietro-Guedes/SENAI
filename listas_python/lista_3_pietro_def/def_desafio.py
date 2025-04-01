#-*- coding: UTF-8 -*-
print('Diga um númeor que direi a quantidade de digitos usados')
num = int(input('Digite o número: '))
while True:
    num1 = num/10
    cont=1
    if num1 == 0:
        break
    print('A quantidade de números é: ', num1)
    
