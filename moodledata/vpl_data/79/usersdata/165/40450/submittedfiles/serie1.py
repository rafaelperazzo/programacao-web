# -*- coding: utf-8 -*-
import math
n=int(input('digite um valor para n:'))
termo=1
soma=0
numerador=1
while termo<=n:
    if termo%2==0:
        soma=soma-numerador//(numerador**2)
    else:
        soma=soma+numerador//(numerador**2)
    numerador=numerador+1
    print('%.5f' %soma)
