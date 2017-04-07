# -*- coding: utf-8 -*-
import math
f=float(input('Digite valor de f:'))
l=float(input('Digite valor de l:'))
Q=float(input('Digite valor de Q:'))
DeltaH=float(input('Digite valor de DeltaH:')) 
V=float(input('Digite valor de v:'))
g=9.81
E=0.000002
D=((8*f*l*(Q**2))/((math.pi**2)*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*V)
K=(0.25)/(math.log10(E/3.7*D)+(5.74/(Rey**0.9)))**2
print('valor de D %.4f' %D)
print('valor de Rey %.4f' %Rey)
print('valor de K %.4f' %K)