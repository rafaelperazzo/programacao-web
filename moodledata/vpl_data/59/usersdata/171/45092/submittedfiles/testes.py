# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o numero de numeros:'))
soma=0
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma+i
print(soma)