# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input ('insira o valor de a:') 
b = input ('insira o valor de b:') 
c = input ('insira o valor de c:') 
d = input ('insira o valor de d:') 

if a>b and b>=c and c>=d or a>b and b<=c and c==d:  
    print ('S')
elif a<b and b>c and c>=d: 
    print ('S') 
elif a<=b and b<c and c>d: 
    print ('S') 
elif a<=b and b<=c and c<d or d>c and c>=b and b==a:
    print ('S') 
else:
    print ('N') 