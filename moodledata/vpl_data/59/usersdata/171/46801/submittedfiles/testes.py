# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite a quantidade de multiplos a serem mostrados:'))
cont=0
for i in range(1,n+1,1):
    x=int(input('digite o numero:'))
    if x%2!=0:
        cont=cont+1
print(x)