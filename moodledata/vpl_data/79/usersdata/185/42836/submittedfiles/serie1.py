# -*- coding: utf-8 -*-
import math
n=int(input('digite a quantidade de termos:'))
soma=0
num=1
den=num**2
for i in range(1,n+1,1):
    soma=soma+(num/den)
    num=num+1
    den=num**2print('%.5f'%soma)

