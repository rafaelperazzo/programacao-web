# -*- coding: utf-8 -*-
import math 
termo=int(input('Digite o valor de n: '))

deno= 1
nume= 1
soma = 0
for termo in range(1,1+n,1):
    if termo%2==0:
        soma=soma-(nume/(deno**2))
    else:
        soma=soma+(nume/(deno**2))
print(soma)

