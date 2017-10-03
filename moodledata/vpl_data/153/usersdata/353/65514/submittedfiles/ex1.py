# -*- coding: utf-8 -*-
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#PROCESSAMENTO
DELTA=(b**2)-(4*a*c)
if DELTA>=0:
    x1=((-b)+(DELTA)**(1/2))/(2*a)
    x2=((-b)-(DELTA)**(1/2))/(2*a)
