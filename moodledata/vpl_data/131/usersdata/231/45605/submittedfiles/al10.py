# -*- coding: utf-8 -*-

n=int(input('digite o número de termos:'))
numerador=2
denominador=1
produto=1
i=0
while (i)<=(n-1):
    produto=(numerador/denominador)*produto
    if i%2==1:
        numerador=numerador+2
    else:
     denominador=denominador+2
    i=i+1
a=produto*2
print('%.5f'%a)

















