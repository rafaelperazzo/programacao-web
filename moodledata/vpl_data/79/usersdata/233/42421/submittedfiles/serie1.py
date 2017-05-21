# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos: '))
numerador=1
denominador=1
soma1=0
soma2=0
termo=1
while termo<=n:
    if n%2==0:
        numerador1=numerador+1
        denominador=numerador**2
        elemento=(numerador/denominador)
        termo=termo+1
        soma1=soma1+elemento
        print(soma1)
    elif n%2==1:
        numerador2=numerador1+1
        denominador=numerador2**2
        elemento=(numerador2/denominador2)
        termo=termo+1
        soma2=soma2+elemento
soma=soma1+soma2
print('%5f'%soma)


