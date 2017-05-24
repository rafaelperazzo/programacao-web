# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
um=a
dois=b
s=um%dois
contador=0
while s!=0:
    um=dois
    dois=s
    s=um%dois
    contador=contador+1
print('mdc(%d,%d)=%d'%(a,b,dois))
print(contador)