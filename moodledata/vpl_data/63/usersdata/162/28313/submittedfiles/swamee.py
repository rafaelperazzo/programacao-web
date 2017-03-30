# -*- coding: utf-8 -*-
import math
f=float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
deltaH=float(input('Digite deltaH:'))
v=float(input('Digite v:'))
g=9.81
E=0.000002
math.pi=3.1415
D=((8*f*L*(Q**2))/((math.pi**2)*g*deltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
k=(0.25)/(math.log10(E/(3.7*D)+(5.74/(Rey**0.9))))
print('O valor de D é %.4f' %D)
print('O valor de Rey é %.4f' %Rey)
print('O valor de k é %.4f' %k)



