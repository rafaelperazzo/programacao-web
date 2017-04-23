# -*- coding: utf-8 -*-
n=int(input('Digite um número inteiro:'))
contador=0
i=2
while i<n:
    if n%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('Primo')
else:
    for i in range(2,n,1):
        print(i)
    print('Não Primo')