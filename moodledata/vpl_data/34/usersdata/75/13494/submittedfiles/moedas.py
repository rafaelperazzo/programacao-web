# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))

if (a>0) and (b>0) and (c>0):
    if (c%a==0) or (c%b==0):
        qa=c//a
        qb=(c%a)//b
        print (qa)
        print (qb)
        
    else:
        print ('N')
        
else:
    print ('N')
