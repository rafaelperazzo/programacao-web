# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o primeiro valor: ')
b=input('Digite o segundo valor: ')
c=input('Digite o terceiro valor: ')
d=input('Digite o quarto valor: ')

if a>b and b>=c>=d :
    print ('S')
elif b>a and b>c>=d :
    print ('S')
elif c>d and c>b>=a :
    print ('S')
elif d>c and c>b>=a :
    print ('S')
else :
    print ('N')
    