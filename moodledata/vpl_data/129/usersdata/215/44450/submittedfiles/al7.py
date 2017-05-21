# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
for i in range(1,n,1):
    if n%i==0:
        print(i)
        soma=soma+i
if soma==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')
        
