# -*- coding: utf-8 -*-
import math
n=int(input('digite um valor para n:'))
termo=1
soma=0
numerador=1
denominador=numerador**2
while termo<=n:
    if termo%2==0:
        soma=soma-numerador//denominador
    else:
        soma=soma+numerador//denominador
    numerador=numerador+1
    termo=termo+1
    print('%.5f' %soma)
