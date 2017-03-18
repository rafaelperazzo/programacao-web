# -*- coding: utf-8 -*-
from __future__ import division


for n in range(1000,10000,1):
    a= n%10
    b= (n//10)%10
    c= (((n//10)//10)%10)
    d= ((((n//10)//10)//10)%10)
    r1= (10*b)+a
    r2= (10*d)+c
    if r1+r2==(n**0.5):
        print n