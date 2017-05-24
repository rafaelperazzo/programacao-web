# -*- coding: utf-8 -*-
import math
m=int(input('digite o número de termos:'))

a=4
pi=0
soma=0
b=2
c=3
d=4
for i in range(0,m,1):
   
    pi=3+(a/(b*c*d))
    if i%2==0:
        soma=soma+pi
    else:
        soma=soma-pi
soma=soma+3
    
print ('%.6d'%soma)

