# -*- coding: utf-8 -*-
import math
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite o valor de DeltaH:'))
v=float(input('Digite o valor de v:'))
g=9.81
Epslon=0.000002
D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**(1/5)
Rey=(4*Q)/(math.pi*D*v)
K=((0.25)/(math.log10(Epslon/3.7*D)+(5.74/Rey**0.9)))**2
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %K)