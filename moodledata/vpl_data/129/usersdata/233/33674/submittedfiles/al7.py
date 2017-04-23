# -*- coding: utf-8 -*-
n=int(input('Digite um número inteiro: '))
soma=0
for i in range(1,n,1):
    if n%1==0:
        print(i)
        soma=soma+i
if soma==n:
    print('PERFEITO')
else:
    print('NÂO PERFEITO')