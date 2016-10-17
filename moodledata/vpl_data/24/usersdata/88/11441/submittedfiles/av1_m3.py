# -*- coding: utf-8 -*-
from __future__ import division
import math
m= input('dê a quantidade de termos: ')
j=4
a=2
b=3
c=4
soma=0
n=a*b*c

while m>0:
    if n%5==0:
        soma= 3 - (j/n)
    
    a=a+2
    b=b+2
    c=c+2
    m=m-1
print ('%.6f' %soma)
    
    
