# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
j=c//a
h=c//b
resta=c%a
restb=c%b
nresta=resta/b
nrestb=restb/a
if c%a==0 and c%b==0 and a>b:
    print('a=%.d'%j)
if c%b==0 and c%a==0 and b>a:
    print('b=%.d'%h)
if c%a!=0 and c%b!=0:
    if resta%b==0:
        print('a=%.d'%j)
        print('b=%.d'%nresta)
    if restb%a==0:
        print('a=%.d'%nrestb)
        print('b=%.d'%h)
    else: 
        print('N')