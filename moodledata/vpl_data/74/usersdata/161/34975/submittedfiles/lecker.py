# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
d=int(input('Digite o valor de d:'))
contador=0
if a>b:
    contador=contador+1
if b>c:
    contador=contador+1
if c>d and c>b:
        contador=contador+1
if contador==1:
    print('S')
else:
    print('N')
    