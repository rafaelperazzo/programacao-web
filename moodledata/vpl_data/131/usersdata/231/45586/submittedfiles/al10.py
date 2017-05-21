# -*- coding: utf-8 -*-

n=int(input('digite o número de termos:'))
numerador=2
denominador=1
produto=1
i=0
while (i)<=(n-1):
    produto=(numerador/denominador)*produto
    if (denominador)>=(numerador):
        numerador=numerador+2
    if (denominador)<=(numerador):
        denominador=denominador+2
    i=i+1
a=produto*2
print(a)

















