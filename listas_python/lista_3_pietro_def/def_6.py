#-*- coding: UTF-8 -*-
print('Olá, diga a temperatura e coloque c para converter para celsiu ou digite f para fahrenheit')
num = int(input('Digite a temperatura: '))
tempInput = input('Você quer conveter para qual temperatura? ')
def temp():
    global tempInput,num
    if tempInput == 'c':
        fah = (num-32) * 5/9
        print(f'A temperatura em celsius é {fah}')
    elif tempInput == 'f':
        cel = 9/5*num+32
        print(f'A temperatura em fahrenheit é {cel}')
    else:
        print('Opção inválida')
temp()
        
