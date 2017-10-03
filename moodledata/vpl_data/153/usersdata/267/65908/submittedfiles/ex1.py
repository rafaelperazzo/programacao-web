# -*- coding: utf-8 -*-
print('A EQUAÇÃO DEVE SER DO TIPO ax²+bx+c')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
#PROCESSAMENTO
delta = b**2-4*a*c
if(delta>=0):
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
    print('x1 = %.2f' x1)
    print('x2 = %.2f' x2)
else:
    print('SRR')
