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
        a1=a1+1
    if c>=b:
        y=c//b
        c=c-(b*y)
        b1=b+1
if c%a==0:
    print('%.f'x)
if c%b==0:
    print('%.f'y)
else:
    print('n')






