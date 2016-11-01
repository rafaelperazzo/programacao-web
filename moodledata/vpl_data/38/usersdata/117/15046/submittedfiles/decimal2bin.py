# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('digite um valor na base binária:'))

a=0
b=1

while n!=0:
    i=i+n%10*b
    n=n//10
    b=b*2
    
    print('%d'%j)