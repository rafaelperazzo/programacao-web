# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite um valor "a":'))
b = int(input('Digite um valor "b":'))
c = int(input('Digite um valor "c":'))
d = int(input('Digite um valor "d":'))

#ordem: a b c d

if a>b and b>=c and c>=d:
    print ('S')
else:
    print ('N')
   
if b>a and b>c and a>=d and c>=d:    
    print ('S')
else:
    print('N')

if c>b and c>d and b>=a and d>=a:
    print('s')
else:
    print('N')
    
if d>c and c>=b and b>=a:
    print ('S')
else:
    print ('N')