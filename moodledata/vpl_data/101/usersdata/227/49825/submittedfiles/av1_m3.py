# -*- coding: utf-8 -*-
import math
m=int(input('digite o número de termos:'))

a=4
pi=0
soma=0

for i in range(0,m,1):
    b=i+1
    c=b+1
    pi=3+(a/(i*b*c))
    if i%2==0:
        soma=soma+pi
    else:
        soma=soma-pi
soma=soma+3
    
print ('%.6d'%soma)

