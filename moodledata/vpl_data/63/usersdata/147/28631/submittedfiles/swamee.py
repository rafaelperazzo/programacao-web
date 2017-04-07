# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g=9.81
epsilon=0.000005
f=float(input('digite valor de f:'))
L=float(input('digite valor de L:'))
Q=float(input('digite valor de Q:'))
deltaH=float(input('digite valor de deltaH:'))
v=float(input('digite valor de v:'))
d=((8*f*L*(Q**2))/((math.pi**2)*g*deltaH))**0.2
rey=(4*Q)/(math.pi*d*v)
k=(0.25)/math.log10((epsilon/(3.7*d))+(5.7/(rey**0.9))**2)
print('o valor de d é %.2f' %d)
print('o valor de rey é %.2f' %rey)
print('o valor de k é %.2f' %k)