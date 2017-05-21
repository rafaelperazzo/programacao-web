# -*- coding: utf-8 -*-
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite DeltaH:'))
v=float(input('Digite o valor de v:'))
g=(9.81)
e=(0.00002)

D=((8*f*L*D*Q*Q)/(math.pi*math.pi*g*DeltaH))**0.2
Rey=(4*Q/math.pi*D*v)
K=0.25/(math.log10*((e/3.7*D+5.74)/(Rey**0.9)))**2

print('valor de D é:%.4f'%D)
print('valor de Rey é:%.4f'%Rey)
print('valor de K é:%.4f'%K)