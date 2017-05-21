# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número inteiro: '))
cont=1
termo=1
numerador=1
denominador=1
n=3
while cont<n:
    termo=termo+(numerador/denominador)
    numerador=numerador+1
    denominador=denominador+n
    n=n+2
    cont=cont+1
print('%.5f'%termo)    
