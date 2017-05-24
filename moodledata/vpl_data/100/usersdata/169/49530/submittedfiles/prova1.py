# -*- coding: utf-8 -*-
import math

a=int(input('Digite o Valor da C1:'))
b=int(input('Digite o Valor da C2:'))
c=int(input('Digite o Valor da C3:'))
d=int(input('Digite o Valor da C4:'))
e=int(input('Digite o Valor da C5:'))

if a<b and b<c and c<d and d<e: 
    print('C')
elif a>b and b>c and c>d and d>e: 
    print('D')
else: 
    print('N')
    