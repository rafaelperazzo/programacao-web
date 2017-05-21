# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número:'))
soma=0
for i in range(0,n,1):
    if n>=0:
        i=i+1
        soma=soma+((i)/(n))
        n=n-1

    else:
        n=((n)*(-1))
        i=i+1
        soma=soma+((i)/(n))
        n=n-1
        
print('%.5f'%soma)

