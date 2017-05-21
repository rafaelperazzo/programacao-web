# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos da sequência:'))
soma=0
numerador=1
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-(numerador/(numerador**2))
    else:
        soma=soma+(numerador/(numerador**2))
    numerador=numerador+1
print('%.5f'%soma)