# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quantidade de divisores a serem mostrados:')
a=input('Número 1:')
b=input('Número 2:')

i=1
c=0

while (c<n):
    if ( i%a==0 or i%b==0):
        print (i)
        c=c+1
    i=i+1
