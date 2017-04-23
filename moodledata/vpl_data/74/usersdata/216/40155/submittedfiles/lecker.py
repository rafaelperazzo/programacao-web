# -*- coding: utf-8 -*-
import math

a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
d=float(input('Digite um número:'))

cont=0


if a>b:
    cont=cont+1
if b>a and b>c:
    cont=cont+1
if c>b and c>d:
    cont=cont+1
if d>c:
    cont=cont+1
    
if cont==1:
    print('S')
if cont!=1:
    print('N')

