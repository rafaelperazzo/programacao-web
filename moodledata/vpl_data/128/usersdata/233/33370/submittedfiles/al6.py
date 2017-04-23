# -*- coding: utf-8 -*-
N=int(input('Digite um número inteiro'))
contador=0
for i in ranger(2,n,1):
    if N%i==0:
    contador=contador+1
    print(i)
if contador==0:
    print('PRIMO')
else:
    print:('NÃO PIRIMO')