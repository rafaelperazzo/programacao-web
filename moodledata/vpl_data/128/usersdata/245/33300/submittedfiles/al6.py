# -*- coding: utf-8 -*-
n=int(input('Digite um número inteiro:'))
contador=0
for i in range(2,n,1):
    if n%i==0:
        contador=contador+1
if contador==0:
    print('primo'%(contador,contador+1,1)
else:
    print('Não Primo')
    