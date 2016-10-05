# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
i=1
if a>=b:
    while i<=b:
        if a%i==0 and b%i==0:
            c=i
        i=i+1
    print(c)  
if b>a:
    while i<=a:
        if b%i==0 and a%i==0:
            c=i
        i=i+1
    print (c)
