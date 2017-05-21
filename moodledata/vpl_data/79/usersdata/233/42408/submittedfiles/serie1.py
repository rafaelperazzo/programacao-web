# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos: '))
cont=0
numerador=1
denominador=1
soma=0
while cont<n
    if n%2==0:
        termo=(numerador/denominador)
        numerador=numerador+1
        denominador=numerador**2
        soma=soma+termo
    if n%2==1:
        termo=(numerador/denominador)
        numerador=numerador+1
        denominador=numerador**2
        soma=soma-termo
print('%5f'%soma)


