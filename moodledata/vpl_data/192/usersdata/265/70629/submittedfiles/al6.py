# -*- coding: utf-8 -*-
n = int(input('digite o valor de n: '))
i=2
contador=0
while (i<n):
    if (n%i)==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('PRIMO')
if contador>0:
    print('NÃO É PRIMO')

    