# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
if a>=b:
    maior=a
else:
    maior=b
i=1
multiplicador=1
while(i<=maior):
    if a%i==0 and b%i==0:
        multiplicador=multiplicador*i
    i=i+1   
print(multiplicador)