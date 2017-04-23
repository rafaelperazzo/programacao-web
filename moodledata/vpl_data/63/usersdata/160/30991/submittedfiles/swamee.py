# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f=float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
DeltaH=float(input('Digite DeltaH:'))
v=float(input('Digite v:'))

g=9.81
E=0.000002

D=( (8*f*L*(Q*Q))/((math.pi*math.pi)*g*DeltaH) )**(1/5)

Rey=(4*Q)/(math.pi*D*v)

K=(0.25)/(math.log10(E/3.7*D+5.74/Rey**0.9)**2

print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %K)

