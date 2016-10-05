# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
n=int(input('Digite o valor de n:'))


i=1

while n>=i:
    if i%a == 0 or i%b == 0:
        print('%d' %i)
        contador=contador+1
        
    i=i+1

