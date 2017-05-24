# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
atual=int(input('digite atual:'))
cont=0
for i in range(2,n,1):
    prox=int(input('digite prox:'))
    if atual!=prox:
        cont=cont+1
    atual=prox
print(cont)
    