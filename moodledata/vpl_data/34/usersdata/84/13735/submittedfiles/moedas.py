# -*- coding: utf-8 -*-
from __future__ import division

a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')

d=c//a
e=(c-(d*a))//b

if c==((a*d)+(b*e)):
    print d
    print e
    
else:
    print('N')
    