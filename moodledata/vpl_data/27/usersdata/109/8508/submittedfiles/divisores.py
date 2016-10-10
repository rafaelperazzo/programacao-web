# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
x=0

for i in range (0,n,1):
    if (a%x)==0 or (b%x)==0:
        print (x)
    x=x+1
