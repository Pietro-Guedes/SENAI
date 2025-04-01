#-*- coding: UTF-8 -*-
print('Diga as notas e a frequência de presença, que direi cê o aluno foi aprovado, reprovado e recuperação')
num1 = float(input('Diga a primeira nota: '))
num2 = float(input('Diga a segunda nota: '))
num3 = float(input('Diga a terceira nota '))
falt = int(input('Diga o número de faltas: '))
nota = (num1+num2+num3) / 3
if falt > 20:
    print('O aluno foi rerovado por falta')
elif nota < 7:
    print('O aluno foi reprovado por nota')
elif nota >= 7:
    print('O aluno foi aprovado')
    
