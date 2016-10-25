# -*- coding: utf-8 -*-
from __future__ import division

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))
c= int(input('Digite o valor de c: '))
cont=0

for i in range (0, c+1, a):
    if (c-i)%b==0:
        qa= i/a
        qb= (c-i)/b
        cont= 1
        
if cont==0:
    print('N')
else:
    print(qa)
    print(qb)
        