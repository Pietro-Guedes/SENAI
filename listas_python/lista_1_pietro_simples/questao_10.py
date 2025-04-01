#-*- coding: UTF-8 -*-
print('Diga três números reais que direi cê é possível fazer um triângulo e qual o tipo dele')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1>num2+num3 or num2>num1+num3 or num3>num1+num2:
    print('Não poderá ser feito um triâgulo')
elif num1 == num2 == num3:
    print('O triângulo é equilatero')
elif num1 == num2 or num1 == num3 or num3 == num2:
    print('O triângulo é isósiles')
elif num1 != num2 != num3:
    print('O triângulo é escaleno')

