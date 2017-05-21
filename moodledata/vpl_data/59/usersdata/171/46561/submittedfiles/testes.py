# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o numero:'))
i=1
soma=0
while n>i:
    if n%i==0:
        soma=soma+i
    i=i+1
if soma==n:
    print('perfeito')
else:
    print('nao e perfeito')
