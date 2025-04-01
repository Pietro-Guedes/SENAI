#-*- coding: UTF-8 -*-
print('Olá, direi o valor líquido do seu salário, de acorodo com as horas trbalhadas')
hora = int(input('Digite as horas trabalhadas: '))
sal = hora*19.5
por = sal*0.9
if sal > 1500:
        print('O seu salário é', por)
else:
    print('O seu salário é', sal)
