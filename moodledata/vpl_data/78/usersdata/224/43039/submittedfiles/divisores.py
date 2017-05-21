# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de números que serão mostrados: '))
a=int(input('Digite o valor a: '))
b=int(input('Digite o valor b: '))
cont=0
i=1
v1=0
v2=0
while cont<n:
    v1=v1+a*i
    v2=v2*b*i
    i=i+1
    if v1==v2:
        cont=cont+1
    else:
        cont=cont+2
    print(v1)
    print(v2)

    