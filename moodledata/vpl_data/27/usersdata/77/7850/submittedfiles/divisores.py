# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Quantidades de divisores a serem mostrados:'))
a=int(input('numero 1:'))
b=int(input('numero 2:'))

i=1
contador=0

while contador<n:
    if i%a == 0 or i%b == 0:
        print('%d' %i)
        contador=contador+1
        
    i=i+1