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
    print(i)
else:
    if e%a==0:
        print(e)
        print(d)
else:
    if c%a==0 and c%b!=0:
        print(c//a)
        print('0')
else:
    if c%b==0 and c%a!=0:
        print('0')
        print(c//b)
elif:
    print ('N')