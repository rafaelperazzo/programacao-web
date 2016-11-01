# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite a: ')
b=input('Digite b: ')
c=input('Digite c: ')

q=c//a
i=c%a
d=c//b
e=c%b
if i%b==0:
    print (q)
    print(i//b)
elif e%a==0:
    print(e)
    print(d)
elif c%b==0 and c%a!=0:
    print('0')
    print(c//b)
else:
    print ('N')