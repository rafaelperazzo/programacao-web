# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite a quantidade de múltiplos:')
a=int(input('Digite um número natural:'))
b=int(input('Digite um número natural:'))
c=0
i=2
while c<n:
    if i%a==0 or i%b==0:
        print (i)
        c=c+1
    i=i+1