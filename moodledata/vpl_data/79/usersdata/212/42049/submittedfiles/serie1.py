# -*- coding: utf-8 -*-
import math
n=float(input('digite o número de termos desejado:'))
n=int(n)
soma=0
termo=1
while termo<=n:
    if (termo%2)==0:
        soma=soma-(termo/(termo**2))
    else:
        soma=soma+(termo/(termo**2))
    termo=termo+1
    
print('%.5f'%soma)
    
