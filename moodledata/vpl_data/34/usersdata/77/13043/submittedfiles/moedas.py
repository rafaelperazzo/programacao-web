# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o valor:'))
b=int(input('Digite o valor:'))
c=int(input('Digite o valor:'))

qa=c//a
x=c-(a*(c%a))
qb=x//b

i=1

while x>0:
    if x//b==0:
        print(qa)
        print(qb)

    else:
        print('N')
        
i=c-1
    
    