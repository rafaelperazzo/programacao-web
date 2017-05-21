# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos: '))
numerador=1
denominador=1
soma=0
termo=1
elemento=0
while termo<=n:
    if n%2==0:
        elemento=elemento+(numerador/denominador)
        numerador=numerador+1
        denominador=numerador**2
        soma=soma+elemento
    if n%2==1:
        elemento=elemento+(numerador/denominador)
        numerador=numerador-1
        denominador=numerador**2
        soma=soma+elemento
print('%5f'%soma)


