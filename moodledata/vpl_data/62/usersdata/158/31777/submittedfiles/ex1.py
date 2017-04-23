# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
delta=(b*b)-(4*a*c)
if delta>=0:
    X1=(-b+delta**0.5)/(2*a)
    print('X1:%.1f'%X1)
    X2=(-b-delta**0.5)/(2*a)
    print('X2:%.1f'%X2)
else:
    print('não existem raízes')