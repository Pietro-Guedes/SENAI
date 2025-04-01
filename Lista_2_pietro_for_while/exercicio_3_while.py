#-*- coding: UTF-8 -*-
print('Olá, diga a idade que direi quantas pessoas te menos que 21 e quantas tem mais de 50')
x = 1
cont21 = 0
cont50 = 0
while True:
    num = int(input('Digite a idade: '))
    if num == -99:
        break
    elif num <= 21:
        cont21 = cont21 + x
    elif num >= 50:
        cont50 = cont50 + x
print(f'Tem {cont21} com menos de 21 anos e {cont50} com mais de 50 anos')
    
    
