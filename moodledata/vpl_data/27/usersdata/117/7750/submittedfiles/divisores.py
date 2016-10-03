# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quantidades de divisores a serem mostrados:')
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=1

while  i<=n:
    if a*i<b*i:
        c=a*i
        print(c)
    if b*i<a*i:
        d=b*i
        print(d)
    i=i+1