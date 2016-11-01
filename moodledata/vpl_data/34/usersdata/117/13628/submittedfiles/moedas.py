# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))

i=c//a
j=c//b
k=c%a
l=c%b

if k//b!=0 or l//a!=0:
    print('N')
else:
    if c%a!=0 and c%b==0 or c%b!=0:
        qa=i
        print (qa)
        qb=k//b
        print (qb)
        
    elif c%b!=0 and c%a!=0 or c%a==0:
        qa=l//a
        print (qa)
        qb=j
        print (qb)