# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#ENTRADA
g = 9.81
E = 0.000002

f = float(input('Digite um valor para f: '))
L = float(input('Digite um valor para L: '))
Q = float(input('Digite um valor para Q: '))
dH = float(input('Digite um valor para dH: '))
v = float(input('Digite um valor para p: '))

#PROCESSAMENTO
D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**0.2
Rey = (4Q)/(math.pi*D*v)
k = (0.25)/((math.log10(E/(3.7*D)+(5.74/(Rey**0.9))))**2)

#SAÍDA
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)