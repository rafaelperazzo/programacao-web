# -*- coding: utf-8 -*-
import math
n=int(input('digite um numero:'))

soma=0
denominador=n
for numerador in range (1,n+1,1):
    soma=soma+numerador/denominador
    denominador=numerador**2
for numerador2 in range (1,n+1,1):
    soma=soma+numerador2/denominador
    denominador=numerador2**2
print('%.5f'%soma)

