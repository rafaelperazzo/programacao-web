# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))

if n>=0:
    n=n
else:
    n=(n*(-1))

S=0
numerador=1
denominador=n
    
for termo in range (1,n+1,1):
    S=S+(numerador/denominador)
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%S)



