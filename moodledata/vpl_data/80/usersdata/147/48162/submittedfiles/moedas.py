# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
r=0
resto=0
if a>b:
    r=c//a
    if c%a!=0:
        resto=(c%a)//b
    print(r)
    print(resto)
if b>a:
    r=c//b
    if c%b!=0:
        resto=(c%b)//a
    print(r)
    print(resto)
if c%b==0:
    b=c//b
    a=a//b
    print(b)
    print(a)
else:
    print('n')
    
    
    
    
    
    