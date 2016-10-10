# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

g=0
if (a<b):
     for i in range ( 0, a, 1):
      if((a%i==0) and (b%i==0)):
          g=i
else:
    for i in range ( 0, b, 1):
      if((a%i==0) and (b%i==0)):
          g=i
print('g')