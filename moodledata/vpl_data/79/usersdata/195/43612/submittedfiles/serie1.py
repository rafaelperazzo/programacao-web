# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
i=0
denominador=1
numerador=1
for i in range (1,n+1,1):
    if i%2==0:
        soma=soma+(numerador)/denominador
    else:
        soma=soma-(numerador)/denominador
    denominador=numerador*numerador
print('%.5f'%soma)    
