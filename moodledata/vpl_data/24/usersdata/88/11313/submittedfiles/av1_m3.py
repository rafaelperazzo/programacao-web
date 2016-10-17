# -*- coding: utf-8 -*-
from __future__ import division
import math
m= input('dê a quantidade de termos: ')
j=4
a=2
b=3
c=4
n=a*b*c

for i in range(0,m+1,1):
    if n%5!=0:
        soma= 3 + (j/n)
    if n%5==0:
        soma= 3 - (j/n)
    a=a+2
    b=b+2
    c=c+2
print ('%.6f' %soma)
    
