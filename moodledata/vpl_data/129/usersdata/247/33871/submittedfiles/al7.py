# -*- coding: utf-8 -*-
n=int(input('digite o numero: '))
contador=0
print('1')
soma = 0
for i in range(2,n,1):
    if n%i==0:
        contador=contador+1
        print('%d'%i)
        soma=soma+i
if soma+1==n:
    print('perfeito')
else:
    print('NÃO PERFEITO')
