# -*- coding: utf-8 -*-
import math
m=int(input('digite o número de termos:'))

a=4
pi=0
soma=0

for i in range(2,m+1,2):
    b=i+1
    c=b+1
    d=i*b*c
    pi=3+(a/(i*b*c))
    if i%2!=0:
        soma=soma+pi
    else:
        soma=soma-pi
    
print ('%.6d'%soma)

