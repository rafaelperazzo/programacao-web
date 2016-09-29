# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
i=1
c=0
if a>=b:
    while i<=b:
        if a%i==0 and b%i==0:
            c=c+1
        i=i+1
print (c)