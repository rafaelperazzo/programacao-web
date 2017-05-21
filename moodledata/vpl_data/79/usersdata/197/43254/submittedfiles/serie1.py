# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos da sequência:'))
soma=o
numerador=1
for termo in range(1,n+1,1):
    if termo%2==0:
        soma=soma-(numerador/(numerador**2))
    else:
        soma=soma+(numerador/(numerador**2))
print(soma)
