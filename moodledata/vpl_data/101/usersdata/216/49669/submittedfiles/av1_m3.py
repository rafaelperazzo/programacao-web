# -*- coding: utf-8 -*-
import math
m=int(input('Digite um valor:'))
soma=3
i=2
for termo in range(2,n+1,1):
    if termo%2==0:
        soma=soma+(4/(i*(i+1)*(i+2)))
        i=i+2
    else:
        soma=soma-(4/(i*(i+1)*(i+2)))
        i=i+2
print(soma)
