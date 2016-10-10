# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Quantidade de termos:')
a=input('Numero 1:')
b=input('Numero 2:')

for i in range(1,n+1,1):
    if a%i==0 or b%i==0:
        print(i)
    i=i+1
