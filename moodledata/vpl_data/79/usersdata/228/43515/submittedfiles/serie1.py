input# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de termos:'))
numerador=1
soma=0
denominador=(numerador*numerador)
for i in range (1,n+1,1):
    if (numerador%2)==0:
        soma=soma-(numerador/denominador)
    else:
        soma=soma+(numerador/denominador)
    numerador=numerador+1
    denominador=numerador*numerador
print('%.5f'%soma)    
