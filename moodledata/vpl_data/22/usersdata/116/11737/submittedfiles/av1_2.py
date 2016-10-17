# -*- coding: utf-8 -*-
from __future__ import division
import math
a = int (input ('insira o primeiro valor:'))
b = int (input ('insira o segundo valor:'))
c = input ('insira o terceiro valor:') 
d = input ('insira o quarto valor:') 

if a!=b and b!=c and c!=d and a==c and b!=d:
    print ('V')
elif a!=b and b!=c and c!=d and a!=c and b==d:
    print ('V')
else:
    print ('F')
