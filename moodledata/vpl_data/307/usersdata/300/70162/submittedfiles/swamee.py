# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Digite f: '))
L = float(input('Digite L: '))
Q = float(input('Digite Q: '))
H = float(input('Digite H: '))
v = float(input('Digite v: '))
g = 9.81
e = 0.000002
D = ((8*f*L*(Q**2))/((math.pi**2)*g*H))**0.2
Rey = (4*Q)/(math.pi*D*v)
k = 0.25/(math.log10((e/3.7D
print('\n')
print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)