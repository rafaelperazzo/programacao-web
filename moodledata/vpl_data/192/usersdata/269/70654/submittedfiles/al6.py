# -*- coding: utf-8 -*-
n=int(input('digite n: '))
i=2
contador=0
while(i<n):
    if n%i==0:
        contador=contador+1
        print(contador)
    i=i+1
if contador>0:
    print('NÃO PRIMO')
else:
    print('PRIMO')