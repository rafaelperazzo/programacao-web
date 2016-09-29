# -*- coding: utf-8 -*-
from __future__ import division
import math
a= input('Digite a:')
b= input('Digite b:')
c= input('Digite c:')
d= input('Digite d:')

if (a>b and b<c and b<d) or (a<b>c and b>d) or (b<c>d and b>a and d<a) or (c<d and c>a and c>b):
    print ('S')
else: 
    print ('N')
    