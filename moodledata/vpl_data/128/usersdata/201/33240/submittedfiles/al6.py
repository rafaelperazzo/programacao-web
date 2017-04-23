# -*- coding: utf-8 -*-
n=int(input('Digite um numero:'))
contador==0
for i in range(2,n,1):
    if n%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('Primo')
else:
    print('Não primo')
