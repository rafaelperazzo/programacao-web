# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
epsilon = 0.000002

f = float(input('Digite o valor de f: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
DeltaH = float(input('Digite o valor de DeltaH: '))
v = float(input('Digite o valor de v: '))

D = float(((8*f*L*(Q**2))/(((math.pi)**2)*g*DeltaH))**(1/5))

Rey = float((4*Q)/((math.pi)*D*v))

k = float((0.25)/((math.log10((epsilon/(3.7*D))+(5.74/(Rey**0.9))))**2))

print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)