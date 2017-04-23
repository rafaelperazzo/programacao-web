# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))

cont=0
if(a>b):
    cont=cont+1
if(b>a) and (b>c):
    cont=cont+1
if(c>b) and (c>d):
    cont=cont+1
if(d>c):
    cont=cont+1
if (cont==1):
    print('s')
else:
    print('n')
