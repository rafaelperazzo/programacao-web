# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número inteiro: '))
soma=0
denominador=n
for numerador in range (1,n+1,n):
    if n<0:
        soma=soma+numerador/(denominador*(-1))
        denominador=denominador-1
    else:
        soma=soma+numerador/(denominador*(-1))
        denominador=denominador-1
print('%.5f'%soma)    


