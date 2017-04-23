# -*- coding: utf-8 -*-
n=int(input('digite um número: '))
contador=0
i=2
while i<n:
    if n%i==0:
        contador=contador+1
        print(n//i)
    i=i+1
if contador==0:
    print('PRIMO')
elif contador!=0:
    print('NÃO PRIMO')