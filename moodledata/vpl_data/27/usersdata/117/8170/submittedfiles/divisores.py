# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quantidades de divisores a serem mostrados:')
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=1
cont=0
while  cont<=n:
    if i%a==0 or b%i==0:
        cont=cont+1
        print(i)
    i=i+1