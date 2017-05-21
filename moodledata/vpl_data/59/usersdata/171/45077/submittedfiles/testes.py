# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite um dado numero a:'))
soma=0
for i in range(1,n+1,1):
    soma=soma+(2**i)
    i=i+1
print(soma)
   