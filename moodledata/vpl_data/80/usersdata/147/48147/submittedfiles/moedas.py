# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
r=0
resto=0
if c//a!=0:
    r=c//a
    if c%a!=0:
        resto=(c%a)//b
    print(r)
    print(resto)
if a%b==0:
    b=c//b
    a=a%b
    print(b)
    print(a)
if c%a!=0 and c%b!=0:
    print('n')
    
    
    
    
    
    