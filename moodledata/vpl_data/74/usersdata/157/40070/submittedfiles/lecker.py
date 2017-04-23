# -*- coding: utf-8 -*-
import math
a=float(input('Valor de A:'))
b=float(input('Valor de B:'))
c=float(input('Valor de C:'))
d=floar(input('Valor de D:'))
cont=0
if a>b:
    cont=cont+1
if b>a and c>d:
    cont=cont+1
if d>c:
    cont=cont+1
if cont==1:
    print('S')
else:
    print('N')
