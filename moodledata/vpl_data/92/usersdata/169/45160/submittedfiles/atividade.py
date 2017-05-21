# -*- coding: utf-8 -*-
import math
n=int(input('Digite 
soma=0
denominador=n
for numerador in range (1,n+1,1):
 soma=soma+numerador/denominador
 denominador=denominador-1
print ('%.5f' %soma)