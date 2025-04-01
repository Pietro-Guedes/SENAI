#-*- coding: UTF-8 -*-
print('Olá, diga a idade da pessoa, que direi a sua faixa etária')
ida = float(input('Digite a idade: '))
if ida < 2:
    print('Essa pessoa é um bebê')
elif ida <= 12:
    print('Essa pessoa é uma criança')
elif ida <= 23:
    print('Essa pessoa é um adolescente')
elif ida <= 70:
    print('Essa pessoa é um adulto')
else:
    print('Essa pessoa é um idoso')
