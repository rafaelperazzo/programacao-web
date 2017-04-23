# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
for i in rage(2,n,1):
    if n%i==0:
        soma=soma+i
if soma==n:
    print('PERFEITO')
else:
    print('NÃO É PERFEITO')