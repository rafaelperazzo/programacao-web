# -*- coding: utf-8 -*-
n=int(input('digite o número:'))
soma=0
cont=1
for i in range(1,n,1):
    if n%i==0:
soma=soma+i
if soma==n:
    print('PERFEITO)
else:
    print('NÃO PERFEITO')