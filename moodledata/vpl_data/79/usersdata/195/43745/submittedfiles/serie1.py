# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
for i in range (1,n+1,1):
    denominador=numerador*numerador
    if i%2!=0:
        soma=soma+(numerador)/denominador
    else:
        soma=soma-(numerador)/denominador
print('s: %.5f'%soma)    
