# -*- coding: utf-8 -*-
n=int(input('digite o valor de n'))
for i in range(1,n,1):
    if n%i==0:
        soma=soma+i
if soma==n:
    print('perfeito')
