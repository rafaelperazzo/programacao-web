# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
soma=0
for i in range (1,n,1):
    if n%i==0:
        soma=soma+1
if soma==n:
    print(i)
    print('perfeito')
    
else:
    print('não perfeito')