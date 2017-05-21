# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Informe o valor a: '))
b=int(input('Informe o valor b: '))
c=int(input('Informe o valor c: '))

i=c//a
for i in range (1,c+1,1):
    x=c-(a*i)
    if x>=b:
        qb=x//b
        if (x%b)==0:
            print(i)
            print(qb)
        else:
            print('N')
    i=i+1
    
