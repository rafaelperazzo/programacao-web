# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
if(a>=b):
    qa=c//a
    qb=(c%a)//b 
    if ((c%a)%b == 0):
        print(qa)
        print(qb)
    else:
        print('N')
    
else:
    qb=c//b
    qa=(c%b)//a
    if((c%b)%a == 0):
        print(qa)
        print(qb)
    else:
        print('N')