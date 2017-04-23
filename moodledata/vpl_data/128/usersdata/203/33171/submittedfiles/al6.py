# -*- coding: utf-8 -*-
n=int(input('digite um número: '))
contador=0
i=2
for i in range (2,n,1):
    if n%i==0:
        contador=contador+1
        print(n//i)
if contador==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')