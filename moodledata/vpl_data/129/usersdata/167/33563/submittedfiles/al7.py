# -*- coding: utf-8 -*-
n=int(input('digite n:'))
contador=0
for i in range (1,n,1):
    if n%i==0:
        soma=soma+1
        print(i)
if soma==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')