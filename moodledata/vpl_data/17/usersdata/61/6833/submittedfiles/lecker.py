# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o primeiro valor: ')
b=input('digite o segundo valor: ')
c=input('digite o terceiro valor: ')
d=input('digite o quarto valor: ')
if a<b<c<d and b<a<d<c and c<a<d<b and d<b<c<a:
    print ('S')
else:
    print ('N')
    