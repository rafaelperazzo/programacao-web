# -*- coding: utf-8 -*-
n=int(input('Informe um número: '))
contador=0
i=(n-1)
while i<n:
    if n%i==0:
        contador=contador+1
        print (i)
    i=i+1
if contador==0:
    print('PRIMO')