# -*- coding: utf-8 -*-
import math
a=float(input('Digite a: '))
b=float(input('Digite b: '))
c=float(input('Digite c: '))
d=float(input('Digite d: '))
cont=0
if (a>b):
    cont=cont+1
if (b>a) and (b>c):
    cont=cont+1
if (c>b) and (c>d):
    cont=cont+1
if (d>c):
    cont=cont+1
if (cont==1):
    print('S')
else:
    print('N')