# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('Digite f:')
L=input('Digite L:')
Q=input('Digite Q:')
DeltaH=input('Digite DeltaH:')
v=input('Digite v:')

D=((((8*f*L*(Q**2))/((math.pi**2)*9.81*DeltaH)))**(1/5))
Rey=(4*Q)/(math.pi*D*v)
k=((0,25)/((math.log10(((0,000002)/(3.7*D))+((5.74)/(Rey**0.9))))**2))

print('D:%.4f'%D)
print('Rey:%.4f'%Rey)
print('k:%.4f'%k)