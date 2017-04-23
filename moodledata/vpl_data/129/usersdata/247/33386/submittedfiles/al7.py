# -*- coding: utf-8 -*-
n=int(input('digite o numero: '))
contador=0
for i in range(2,n,0):
    if n%i==0:
        contador=contador+1
        print('%d'%i)
