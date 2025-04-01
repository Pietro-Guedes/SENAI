#-*- coding: UTF-8 -*-
print('Olá, diga a altura e o raio de um cilindro, que direi o volume')
base = float(input('Digite a raio: '))
alt = float(input('Digite a altura: '))
def mult(base, alt):
    vol = (3.14*(base*base)) * alt
    print('A área é %.2f' %vol)
mult(base, alt)
           
