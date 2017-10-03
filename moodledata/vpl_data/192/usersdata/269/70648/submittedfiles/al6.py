# -*- coding: utf-8 -*-
n=int(input('digite n: '))

while(i<n):
    if n%i==0:
        contador=contador+1
        print(contador)
    i=i+1
if contador>0:
    print('NÃO PRIMO')
else:
    print('PRIMO')