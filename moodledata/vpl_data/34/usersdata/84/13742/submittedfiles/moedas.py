# -*- coding: utf-8 -*-
from __future__ import division

a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')

d=c//a
e=(c-(d*a))//b
f=0
g=c//b

if c==((a*d)+(b*e)):
    print d
    print e
if c==(b*g):
    print f
    print g
    
else:
    print('N')
    