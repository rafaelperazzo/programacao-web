# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor da primeira moeda:'))
b=int(input('Digite o valor da segunda moeda:'))
c=int(input('Digite o valor da célula:'))
i=c//a
for i in range(0,c,1):
    p=c-(a*i)
    qb=p//b  
    if p%b!=0:
        print('N')
    else:
        print(i)
        print(qb)
