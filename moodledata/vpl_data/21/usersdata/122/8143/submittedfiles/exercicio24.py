# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

a=input('Digite o valor de a:')
b+input('Digite o valor de b:')

for i in range (1,(a*b),1):
    if i%a==0 and i%b==0:
        print i
        break
