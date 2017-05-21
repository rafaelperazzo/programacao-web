# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a  : '))
b=float(input('Digite o valor de  b : '))
c=float(input('Digite o valor de  c : '))
DELTA=(b*b)-(4*a*c)
if DELTA>0:
    X1=(-b+DELTA)/2*a
    X2=(-b-DELTA)/2*a
    print('X1=%.2f'%X1)
    print('X2=%.2f'%X2)    
else:
    print('SRR')