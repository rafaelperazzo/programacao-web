# -*- coding: utf-8 -*-
x=int(input('Digite um valor:'))
contador=0
for i in range (2,x,1):
    if x%i==0:
        contador=contador+1
    i=i+1
    print(i)
