# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
soma=0
for i in range (1,n,1):
    if n%i==0:
        soma=soma+1
        print(i)
        if soma==n:
            print('perfeito')
    
if soma!=0
    print('não perfeito')