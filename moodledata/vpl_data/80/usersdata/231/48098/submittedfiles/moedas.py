# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite moedas:'))
b=int(input('digite moedas:'))
c=int(input('cedulass:'))
a1=0
b1=0
w=c
for i in range(1,c,1):
    if c>=a:
        n=c//a
        c=c-(a*n)
        a1=a1+n
    if c>=b:
        d=c//b
        c=c-(d*b)
        b1=b1+d
   if c>=a:
        c=c-a
        a1=a1+1
    if c>=b:
        c=c-b
        b1=b1+1
    
    if c>=b:
        d=c//b
        c=c-(d*b)
        b1=b1+d
if (a1*a)+(b1*b)-w==0:
    print(a1)
    print(b1)
else:
    print('n')







