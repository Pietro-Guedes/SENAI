#-*- coding: UTF-8 -*-
print('Diga o seu salário, o quanto quer de empréstimo e quantas parcelas vai ser paga, que eu direi cê é possível fazer')
emp = int(input('Diga o valor de empréstimo: '))
sal = float(input('Diga seu salário: '))
mes = int(input('Diga em quantos meses será pago: '))
par = (sal*30) / 100
par1 = emp / mes
if par > par1:
    print('O seu empréstimo foi aprovado')
else:
    print('O seu empréstimo não foi aprovado')
