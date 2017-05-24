# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite moedas:'))
b=int(input('digite moedas:'))
c=int(input('cedulass:'))
a1=0
b1=0
for i in range(1,c,1):
    if c>=a:
        x=c//a
        c=c-(a*x)
        a1=a1+x
    elif c>=b:
        y=c//b
        c=c-(b*y)
        b1=b1+y
    elif c>=a:
        c=c-a
        a1=a1+1
        
if (a1*a)+(b1*b)==c:
    print(a1)
    print(b1)
else:
    print('n')







