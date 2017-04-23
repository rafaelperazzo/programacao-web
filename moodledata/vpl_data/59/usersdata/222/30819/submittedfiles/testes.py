# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n: '))
i=2
contador=0
while i<n:
    if n%i==0:
        contador=contador+1
        print(i)
    i=i+1
print(contador)