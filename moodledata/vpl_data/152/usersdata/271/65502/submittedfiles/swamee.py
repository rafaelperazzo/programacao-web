# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
#ENTRADA
f = float(input('Digite o valor de f: '))
l = float(input('Digite o valor de l: '))
q = float(input('Digite o valor de q: '))
DeltaH = float(input('Digite o valor de DeltaH: '))
v = float(input('Digite o valor de v: '))
g = 9.81
e = 0.000002
#PROCESSAMENTO
D = ((8*f*l*q*q)/(math.pi*math.pi*g*DeltaH))**(1/5)
Rey = (4*q)/(math.pi*D*v)
k = (0.25)/((math.log10((e)/(3.7*D)+(5.74)/(Rey**0.9)))**2)
#SAIDA
print('O valor de D: %.4f' % D)
print('O valor de Rey: %.4f' % Rey)
print('O valor de k: %.4f' % k)