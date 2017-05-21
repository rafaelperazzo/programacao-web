# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a'))
b=float(input('Digite o valor de b'))
c=float(input('Digite o valor de c'))
x=float(input('Digite o valor de x'))
Delta=(b**2)-4*a*c
if Delta<0:
    print('SRR')
else:
    x1=(-b+(Delta**0.5))/2*a
    x2=(-b-(Delta**0.5))/2*a
    print('x1=%.2f'%x1)
    print('x2=%.2f'%x2)