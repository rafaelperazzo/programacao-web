# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
i=0
y=c//a
while i<c:
    x=c-(a*y)
    if x>=b:
        qb=x//b
        if (x%b)==0:
            print(y)
            print(qb)
        else:
            print('N')
    i=i+1
    
    
        
    
