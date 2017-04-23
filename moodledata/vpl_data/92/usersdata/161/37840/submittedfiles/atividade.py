# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos:'))
if n>=0:
    n=n
else:
    n=(n*(-1))
    
denominador=n
soma=0
for i in range(1,n+1,1):
    soma=soma+(i/denominador)
    i=i+1
    denominador=denominador-1
print('%.5f'%soma)
    
