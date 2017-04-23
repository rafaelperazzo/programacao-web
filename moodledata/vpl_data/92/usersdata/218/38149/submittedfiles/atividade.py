# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
if n<0:
    n=n*(-1)
numerador=0    
denominador=n
soma=0
cont=1
while cont<=n:
    soma=soma+(cont/denominador)
    cont=cont+1
    denominador=denominador-1
print('%.5f'%soma)    