# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))

d=c//a
e=c//b
f=c%a
g=c%b

if c%a!=0 and f%b!=0:
    qa=d
    print (qa)
    qb=f//b
    print (qb)
        
elif c%b!=0 and f%a!=0:
    qa=e
    print (qa)
    qb=g//a
    print (qb)
    
else:
    print ('N')