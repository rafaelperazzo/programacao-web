# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))

i=c//a
for i in range (1,c+1,1):
    x=c-(a*i)
    if x>=b:
        qb=x//b
        if x%b==0:
            print(i)
            print(qb)
        else:print('N')
    i=i+1    
    


