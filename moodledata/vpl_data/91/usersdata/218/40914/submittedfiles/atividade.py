# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
termo=n
contador=0
while termo>0:
    termo=termo//10
    contador=contador+1
print(contador)    