# -*- coding: utf-8 -*-
import math

n=int(input('Digite n:'))
soma=0
denominador=n
for numerador in range (1,n+1):
    soma=soma+numerador/denominador
    denominador=denominador-1
print(soma)
