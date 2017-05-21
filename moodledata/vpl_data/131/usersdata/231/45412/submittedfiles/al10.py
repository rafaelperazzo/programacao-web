# -*- coding: utf-8 -*-

n=int(input('digite o número de termos:'))
numerador=2
denominador=1
produto=1
i=0
while (i)<=n:
    produto=(produto*numerador)/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denominador=denomidor+2
    i=i+1
print(produto)

















