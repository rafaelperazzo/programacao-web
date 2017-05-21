# -*- coding: utf-8 -*-
import math
n=int(input('digite a quantidade de termos:'))
soma=0
num=1
den=num**2
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-(num/den)
    else:
        soma=soma+(num/den)
    num=num+1
    den=num**2
print('%.5f'%soma)

