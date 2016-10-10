# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('insira o valor de n:') 
a = input ('insira o valor de a:')
b = input ('insira o valor de b:')

for i in range (1,n+1,1):
    if i%a==0 and i%b==0:
        print i
    elif i%a==0:
        print i
    elif i%b==0:
        print i 