# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

for i in range (1,(a*b),1):
    if a%i==0 and b%i==0:
        print(i)