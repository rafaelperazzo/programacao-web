# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite um dado numero n:'))
soma=0
i=1
while n>i:
   if n%2==0:
       soma=soma+i
   i=i+1
if soma==n:
    print('perfeito')
else:
    print('nao perfeito')
   