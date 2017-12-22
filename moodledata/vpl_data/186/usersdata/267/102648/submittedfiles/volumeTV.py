# -*- coding: utf-8 -*-
 
v=int(input('Volume inicial: '))
t=int(input('Número de modificações: '))
 
for i in range(0,t,1):
    m=int(input(('Modificação: '))
    v=v+m
    se v>100:
        v=100
    se v<0:
        v=0
print(v)