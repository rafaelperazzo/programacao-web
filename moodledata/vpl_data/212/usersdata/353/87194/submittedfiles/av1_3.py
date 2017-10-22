# -*- coding: utf-8 -*-
import math
a=int(input('Valor 1:'))
b=int(input('Valor 2:'))
c=int(input('Valor 3:'))

i=1
s=0

while(i<a) and (i<b) and (i<c):
    if (a%i==0) and (b%i==0) and (c%i==0):
        s=s+(i*i)
        i=i+1
        print (s)
    
