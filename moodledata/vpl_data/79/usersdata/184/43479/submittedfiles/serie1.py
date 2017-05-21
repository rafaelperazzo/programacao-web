# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
termo=1
numerador=1
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-numerador/(numerador**2)
        numerador=numerador+1
    else:
        soma=soma+numerador/(numerador**2)
        numerador=numerador+1
print('soma: %.5f' %soma)

