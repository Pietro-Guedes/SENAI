#-*- coding: UTF-8 -*-
print('Diga dois valores inteiros, que eu direi qual maior em ordem crescente')
a = int(input('Diga o primeiro valor: '))
b = int(input('Diga o segundo valor: '))
if b > a:
    c = a
    a = b
    b = c
print('O maior valor é %i e o menor é %i' %(a,b))
