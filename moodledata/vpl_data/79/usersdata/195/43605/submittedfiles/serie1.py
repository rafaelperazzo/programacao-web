# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
denominador=4
numerador=2
denominador=numerador*numerador
for i in range (1,n+1,1):
        soma=soma+(numerador*numerador)/denominador
        denominador=numerador*2
print('%.5f'%soma)    
