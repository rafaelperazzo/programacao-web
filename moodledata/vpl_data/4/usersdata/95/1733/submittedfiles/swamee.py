# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('0.2')
L=input('50000')
Q=input('0.65')
DeltaH=input('22')
v=input('0.000001')

D=float((((8*f*L*(Q**2))/((math.pi**2)*9.81*DeltaH)))**(1/5))
Rey=float(4*Q)/(math.pi*D*v)
k=float((0,25)/((math.log10(((0,000002)/(3.7*D))+((5.74)/(Rey**0.9))))**2))

print('D:%.4f'%D)
print('Rey:%.4f'%Rey)
print('k:%.4f'%k)