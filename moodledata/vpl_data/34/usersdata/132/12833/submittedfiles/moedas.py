# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
qa=c//a
if qa!=0:
    qb=(c%a)//b
    print(qa)
    print(qb)
if qa==0:
    qb=c//b
    print(qa)
    print(qb)
if qa!=0:
    qb=(c%a)//b
    if qb==0:
        print('N')
    
    
    