# -*- coding: utf-8 -*-
import math

a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
d=float(input('Digite um número:'))

cont=0

if a>b and a>d:
    cont=cont+1
elif b>a and b>c:
    cont=cont+1
elif c>b and c>d:
    cont=cont+1
elif d>c and d>a:
    cont=cont+1
    
else:
    if cont==1:
        print('S')
    if cont!=1:
        print('N')

