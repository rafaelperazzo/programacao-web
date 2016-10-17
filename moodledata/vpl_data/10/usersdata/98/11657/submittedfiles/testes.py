# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n: ')
j=input('Digite o valor de j: ')
m=input('Digite o valor de m: ')
cont=0
i=0
while True:
    a=i%m
    b=j%m
    i=i+1
    if a==b:
        print(a)
        cont=cont+1

    if cont==n:
        break