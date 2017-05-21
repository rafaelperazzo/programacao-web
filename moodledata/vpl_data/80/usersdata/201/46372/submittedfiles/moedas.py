# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite um valor:'))
b=int(input('Digite um valor:'))
c=int(input('Digite um valor:'))
i=c//a
while a>0:
    x=c-(i*a)
    if x>=b:
        qb=x//b
        if x%b==0:
            print(i)
            print(qb)
        else:
            print('N')
    i=i+1
