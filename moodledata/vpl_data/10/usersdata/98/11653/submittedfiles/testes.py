# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
i=input('Digite o valor de i: ')
j=input('Digite o valor de j: ')
m=input('Digite o valor de m: ')
cont=0

while True:
    a=i%m
    b=j%m
    if a==b:
        print(a)
        cont=cont+1
    else:
        i=i+1
    if cont==n:
        break