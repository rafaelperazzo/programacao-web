# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número inteiro: '))
soma=0
denominador=n
for numerador in range (1,n+1,n):
    soma=soma+numerador/denominador
    denominador=denominador-1
print(soma)    


