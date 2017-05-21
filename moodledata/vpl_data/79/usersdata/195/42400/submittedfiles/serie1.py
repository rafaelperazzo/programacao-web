# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
termo=1
numerador=1
denominador=numerador*numerador
for i in range (1,n+1,1):
    if i%2==0:
        soma=soma+(numerador*numerador)/denominador
    else:
        soma=soma-(numerador*numerador)/denominador
    denominador=numerador*2
print('%.5f'%soma)    
