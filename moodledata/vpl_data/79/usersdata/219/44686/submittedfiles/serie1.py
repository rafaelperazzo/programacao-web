# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
soma=0
termo=1
d=1
for numerador in range (1,n+1,1):
    if termo%2==0:
        soma=soma-(numerador)/(numerador**2)
    else:
        soma=soma+(numerador)/(numerador**2)
        d=numerador**2
print('%.5d' %soma)

