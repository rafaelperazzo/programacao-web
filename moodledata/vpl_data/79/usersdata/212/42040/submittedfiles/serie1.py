# -*- coding: utf-8 -*-
import math
n=float(input('digite o número de termos desejado:'))
n=int(n)
cont=1
soma=0
termo=1
while cont<n:
    if (termo%2)==0:
        soma=soma-(termo/(termo**2))
    else:
        soma=soma+(termo/(termo**2))
    cont=cont+1
print('%.5f'%soma)
    
