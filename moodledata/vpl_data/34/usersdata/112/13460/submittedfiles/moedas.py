# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
j=c//a
h=c//b
resta=c%a
restb=c%b
if c%a==0:
    print('a=%.d'%j)
if c%b==0:
    print('b=%.d'%h)
print('S')    
else: 
    print('N')