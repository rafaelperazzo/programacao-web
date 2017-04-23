# -*- coding: utf-8 -*-
import math
f=float(input('f:'))
L=float(input('L:'))
Q=float(input('Q:'))
DeltaH=float(input('DeltaH:'))
v=float(input('v:'))
g=9.81
e=0.000002
D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**(1/5)
Rey=(4*Q)/(math.pi*D*v)
A=0.25/((math.log10((e/3.7*D)+(5.74/(Rey**0.9))))**2)
print('D:%.4f'%D)
print('Rey:%.4f'%Rey)
print('A:%.4f'%A)