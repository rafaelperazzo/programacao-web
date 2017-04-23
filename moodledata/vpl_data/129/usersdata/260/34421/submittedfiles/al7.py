# -*- coding: utf-8 -*-
n = int( input('digite um valor interio'))
contador= 0
a=0
for i in range (1,n,1):
    if n%i == 0:
        contador= contador + 1
        print(i)
        a=i+a
if a==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')