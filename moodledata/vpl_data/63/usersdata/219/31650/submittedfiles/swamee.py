# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite f:'))
l=float(input('Digite l:'))
q=float(input('Digite q:'))
dh=float(input('Digite dh:'))
V=float(input('Digite V:'))
e=0.000002
g=9.81
D=(((8*f*l(q**2)))/((math.pi**2)*g*dh))**0.2
Rey=(4*Q)/(math.pi*D*V)
k=(0.25)/(math.log((((e)/(3.7*D)))+((5.74)/(Rey)**0.9)))**2
print('%4.f' %D)
print('%4.f' %Rey)
print('%.f' %k)

