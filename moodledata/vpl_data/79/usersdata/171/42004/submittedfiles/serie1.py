# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
denominador=1
for numerador in range(1,n+1,1):
    soma=soma+(numerador/denominador)
    denominador=numerador*numerador

print('%.5f'%soma)
    