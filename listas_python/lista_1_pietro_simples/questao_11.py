#-*- coding: UTF-8 -*-
print('Diga as notas do aluno que direi cê ele está aprovado, reprovado ou de recuperação')
not1 = float(input('Diga a primeira nota: '))
not2 = float(input('Diga a segunda nota: '))
med = (not1+not2) / 2
if med < 3:
    print('O aluno está reprovado')
elif med < 7:
    print('O aluno está de recuperação')
elif med >= 7:
    print('O aluno está aprovado')
