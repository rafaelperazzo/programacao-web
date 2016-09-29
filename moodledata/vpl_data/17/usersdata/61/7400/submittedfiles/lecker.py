# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o primeiro valor: ')
b=input('digite o segundo valor: ')
c=input('digite o terceiro valor: ')
d=input('digite o quarto valor: ')
if a>b and b<c and c>d:
    print ('S')
    if b>a and b>c and d<c:
        print ('S')
    if c>b and c>d and a<b:
        print ('S')
    if d>c and c>b and a<b:
        print ('S')
else:
    print ('N')
    