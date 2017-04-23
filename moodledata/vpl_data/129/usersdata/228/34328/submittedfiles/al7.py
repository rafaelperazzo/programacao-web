# -*- coding: utf-8 -*-
n=int(input('digite um valor:'))
soma=0
contador=0
for i in range(1,n,1):
    if n%i==0:
        contador=contador+i
        soma=soma+1
        print(soma)
        
if contador==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')
        
        