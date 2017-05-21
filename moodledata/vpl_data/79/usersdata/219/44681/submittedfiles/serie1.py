# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
soma=0
denominador=1
for numerador in range (1,n+1,1):
    if (numerador/denominador)%2==0:
        soma=soma-(numerador)/(numerador**2)
    else:
        soma=soma+(numerador)/(numerador**2)
    denominador=numerador**2
print('%.5d' %soma)

