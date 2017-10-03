# -*- coding: utf-8 -*-
n = int(input('digite o valor de n: '))
i=1
contador=0
while (i<n):
    if (n%i)==0:
        contador=contador+1
    i=i+1
    print(contador)
if contador==n:
    print('PERFEITO')
else :
    print('NÃO PERFEITO')
    