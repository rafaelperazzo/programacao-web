# -*- coding: utf-8 -*-
import math
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite DeltaH:'))
v=float(input('Digite o valor de v:'))
g=float(9.81)
e=float(0.00002)

D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
K=0.25/(math.log10((e/(3.7*D))+(5.74)/(Rey**0.9)))**2

print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('K=%.4f'%K)