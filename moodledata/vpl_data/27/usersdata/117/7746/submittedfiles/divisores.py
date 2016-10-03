# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quantidades de divisores a serem mostrados:')
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=1

while  i<=n:
    if a>0 and b>0:
        c=i*a
        print(c)
    i=i+1