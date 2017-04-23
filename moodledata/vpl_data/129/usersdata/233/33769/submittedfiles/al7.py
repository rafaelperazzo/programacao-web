# -*- coding: utf-8 -*-
n=int(input('Digite um número inteiro: '))
contador=0
soma=0
for i in range(2,n,1):
    if n%i==0:
        contador=contador+1
for i in range(1,n,1):
    if n%i==0:
        print(i)
        soma=soma+i
if soma==n:
    print('PERFEITO')
else:
    print('NÂO PERFEITO')