# -*- coding: utf-8 -*-
import math

a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
d=int(input('Digite um número:'))

cont=0
    if a>b and a>d:
        cont=cont+1
    if b>a and b>c:
        cont=cont+1
    if c>b and c>d:
        cont=cont+1
    if d>c and d>a:
        cont=cont+1

if cont==1:
    print('S')
else:
    print('N')

