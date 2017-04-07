# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('digite a'))
b=float(input('digite b'))
c=float(input('digite c'))
DELTA=(b*b)-4*a*c
x1=(-b+(DELTA)**(1/2))/2*a
x2=(-b-(DELTA)**(1/2))/2*a
if DELTA>=0:
    print('x1')
    print('x2')
else:
    print('SRR')