# -*- coding: utf-8 -*-
n=int(input('digite o numero: '))
contador=0
print('')
soma = 0
for i in range(0,n,1):
    if n%i==0:
        contador=contador+1
        print('%d'%i)
        soma=soma+i
if soma==n:
    print('perfeito')
else:
    print('NÃO PERFEITO')
