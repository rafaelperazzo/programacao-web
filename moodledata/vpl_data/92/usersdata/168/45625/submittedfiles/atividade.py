# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número inteiro: '))
soma=0
denominador=n
for numerador in range (1,n+1,1):
    if n<0:
        denominador=denominador*(-1)
        soma=(soma+numerador)/denominador
        denominador=denominador-1
    else:
        soma=(soma+numerador)/denominador
        denominador=denominador-1
print('%.5f'%soma)    


