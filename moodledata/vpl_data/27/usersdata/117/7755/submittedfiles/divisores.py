# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quantidades de divisores a serem mostrados:')
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=1

while  i<=n:
    if a<b:
        c=a*i 
        print(c)
        d=b*i
        print(d)
    if b<a:
        d=b*i
        print(d)
        c=a*i 
        print(c)
    i=i+1