# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
numerador=1
denominador=1
soma=0
for numerador in range(1,n+1,1):
    soma=soma+(numerador/denominador)
    denominador=numerador**2
    if numerador%2!=0:
        soma=soma-(numerador/denominador)
    elif numerador%2==0:
        soma=soma+(numerador/denominador)
print(soma)
    