# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número inteiro: '))
termo=1
numerador=1
denominador=1
mudança=3
while termo<n:
    termo=termo+(numerador/denominador)
    numerador=numerador+1
    denominador=denominador
print(termo)    
