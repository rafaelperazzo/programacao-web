# -*- coding: utf-8 -*-
n=int(input('Digite um número inteiro: '))
contador=0
for i in range (2,n,1):
    if n%i==0:
        print(i)
    print('Não Primo')
if n%i!=0:
    print('Primo')