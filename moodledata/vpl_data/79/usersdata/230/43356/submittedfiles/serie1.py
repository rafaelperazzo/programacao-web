# -*- coding: utf-8 -*-
import math
n=int(input('Digite quantidade de termos: '))
soma=0
denominador=n
for numerador in range (1,n+1,1):
    soma=soma+numerador/denominador
    denominador=denominador**2
print('%.5f' %soma)