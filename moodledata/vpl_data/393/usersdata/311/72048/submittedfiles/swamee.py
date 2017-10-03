# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite o valor de f:'))
L= float(input('Digite o valor de L:'))
Q= float(input('Digite o valor de Q:'))
H= float(input('Digite o valor de H:'))
v= float(input('Digite o valor de v:'))
pi= math.pi
g= 9.81
e= 0.000002
D= ((8*f*L*(Q**2))/((pi**2)*g*H))**0.2
Rey= (4*Q)/(pi*D*v)
k= [0.25/math.log10(((e/(3.7*D))+(5.74/(Rey**0.9)))**2)]
print '%.4F' % D
print '%.4F' % Rey
print '%.4F' % k
