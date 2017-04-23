# -*- coding: utf-8 -*-
import math
f=float(input('valor de f:'))
L=float(input('valor de L:'))
Q=float(input('valor de Q:'))
DeltaH=float(input('valor de DeltaH:'))
v=float(input('valor de v:'))
g=9.81
E=0.000002
math.pi=3.1416
D=((8*f*L*Q**2)**2//5)//((math.pi**2*g*DeltaH))**2//5
REY=(4*Q)/(math.pi*D*v)
k=(0.25)//(math.log10(e//3.7+5.74//REY**0.9))
print('D=')
print('REY:')
print('k:')