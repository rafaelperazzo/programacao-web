# -*- coding: utf-8 -*-
import math
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite deltaH'))
v=float(input('digite v:'))
g=9.81
E=0.000002
D=((8*f*l*q**2)/(math.pi**2*g*deltaH))**0.2
Rey=(4*q)/(math.pi*D*v)
K=(0.25)/((math.log10((E/3.7*D)*(5.74/Rey**0.9))))**2
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%k)