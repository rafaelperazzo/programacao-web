# -*- coding: utf-8 -*-
n=int(input('digite o valor dos termos:'))
numerador=2
denominador=1
produto=1
whille i<=(n-1):
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denominador=denominador+2
    i=i+1
