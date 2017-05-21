# -*- coding: utf-8 -*-
import math
soma=0
n=int(input('digite n: '))
numerador=1
denominador=1
for i in range(1,n+1,1):
    if i%2!=0:
        soma=soma+(numerador/denominador)
        numerador=numerador+1
        denominador=(numerador**2)
    else:
        soma=soma-(numerador/denominador)
        numerador=numerador+1
        denominador=(numerador**2)
print('%.5f' %soma)
