# -*- coding: utf-8 -*-
import math
f=float(input('digite f:'))
L=float(input('digite L:'))
Q=float(input('digite Q:'))
deltaH=float(input('digite deltaH:'))
v=float(input('digite v:'))
g=9.81
E=0.000002
D=((8*f*L*(Q)**2)/((math.pi)**2*g*deltaH))**1/5
print('D:%.4f'%D)
Rey=(4*Q)/(math.pi*D*v)
print('Rey:%.4f'%Rey)
K=(0,25)/(math.log10((E/(3.7*D))+(5.75)/(Rey**0.9))**2
print('K:%.4f'%K)