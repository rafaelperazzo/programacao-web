# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite f :'))
L=float(input('Digite L :'))
Q=float(input('Digite Q :'))
DeltaH=float(input('Digite DeltaH :'))
v=float(input('Digite v :'))
e=0.000002
g=9.81
D=((8*f*L(Q**2))/(math.pi**2)*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
k=(0.25)/(math.log((((e)/(3.7*D)))+((5.74)/(Rey)**0.9)))**2
print('%4.f' %D)
print('%4.f' %Rey)
print('%.f' %k)

