# -*- coding: utf-8 -*-
n=int(input('digite n: '))
i=2
soma=1
while(i<n):
    if n%i==0:
        soma=soma+i
    print(soma)    
    i=i+1    
if soma>n or soma<n:
    print('NÃO PERFEITO')
if soma==n:
    print('PERFEITO')