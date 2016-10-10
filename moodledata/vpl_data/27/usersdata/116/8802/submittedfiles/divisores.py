# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('insira o valor de n:') 
a = input ('insira o valor de a:')
b = input ('insira o valor de b:')

i=1

for j in range (0,n,1):
    while True: 
        if i%a==0 or i%b==0:
            print i
        if i%a==0 and i%b==0:
            print i
        break 
    