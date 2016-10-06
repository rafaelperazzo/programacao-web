# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite a quantidade de múltiplos:')
a=int(input('Digite um número natural:'))
b=int(input('Digite um número natural:'))
i=1
while i<=n:
    c=a*i
    d=b*i
    i=i+1
    print (c,d)