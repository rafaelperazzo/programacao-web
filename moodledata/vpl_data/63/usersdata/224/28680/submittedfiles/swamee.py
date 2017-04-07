# -*- coding: utf-8 -*-
import math
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite o valor de DeltaH:'))
v=float(input('Digite o valor de v:'))
D=((8*f*L*Q*Q)/(math.pi*math.pi*9.81*DeltaH))**(1/5)
print('D=:%4.f'%D)
Rey=(4*Q)/(math.pi*D*v)
print('Rey=:%4.f'%Rey)
k=(0.25)/((math.log10((0.000002/(3.7*D)+(5.74/(Rey**0.9)))**2
print('k=: %4.f'%k)

