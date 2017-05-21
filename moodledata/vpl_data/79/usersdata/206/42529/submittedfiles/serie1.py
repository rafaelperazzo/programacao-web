# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de termos:'))
s=0

for i in range (1,n+1,1):
    if (i%2==1):
        s= s+(i/i**2)
    else (i%2==0):
        s= s-(i/i**2)
print('%.5f' %s) 
        
    