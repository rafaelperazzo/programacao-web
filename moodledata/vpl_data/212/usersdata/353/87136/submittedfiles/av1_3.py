# -*- coding: utf-8 -*-
import math
a=int(input('Valor 1:'))
b=int(input('Valor 2:'))
c=int(input('Valor 3:'))

i=0
s=0

while(i>0):
    if (a%i==0) and (b%i==0) and (c%i==0):
        s=s+i
        i=i+1
        print (s)
    
