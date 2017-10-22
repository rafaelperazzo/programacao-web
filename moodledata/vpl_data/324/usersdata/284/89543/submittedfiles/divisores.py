# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de multiplos: '))
a=int(input('digite o valor: '))
b=int(input('digite o valor: '))
for n in range(1,n/2+1,1):
    if(a*n!=b*n):
        DIVISORES=(a*n)
        DIVISORES=(b*n)
print(DIVISORES)
    
    