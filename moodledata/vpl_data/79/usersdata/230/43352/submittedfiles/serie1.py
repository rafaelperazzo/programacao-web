# -*- coding: utf-8 -*-
import math
n=float(input('Digite quantidade de termos: '))
soma=0
denominador=1
for numerador in range (1,n+1,1):
    soma=soma+numerador/denominador
    denominador=denominador**2
print('%.5f' %soma)