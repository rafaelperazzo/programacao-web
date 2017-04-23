# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
contador=0
if a>b:
    contador=contador+1
if b>a and b>c:
    contador=contador+1
if c>b and c>d:
    contador=contador+1
if d>c:
    contador=contador+1
if contador==1:
    print('S')
else:
    print('N')
    