# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
if a>=b:
    menor=b
else:
    menor=a
i=2
multiplicador=1
while(i<=menor):
    if a%i==0 and b%i==0:
        multiplicador=multiplicador*i
    i=i+1   
print(multiplicador)