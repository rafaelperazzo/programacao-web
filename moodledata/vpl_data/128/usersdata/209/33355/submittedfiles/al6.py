# -*- coding: utf-8 -*-
x=int(input('Digite um valor:'))
contador=0
for i in range (2,x,1):
    if x%i==0:
        contador=contador+1
        print(i)
contador=0
i=2
while i<x:
    if x%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('PRIMO')
else:
    print('NAO PRIMO')
