# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Quantidades de divisores a serem mostrados:'))
a=int(input('numero 1:'))
b=int(input('numero 2:'))

mult=1
contador=0

while contador<n:
    if mult%a == 0 or mult%b == 0:
        print('%d' %mult)
        contador=contador+1
        
    mult=mult+1