# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
a=int(input('digite a:'))
soma=0
while a>=1:
    i=a//10
    r=i%10
    soma=soma+r
    a=a//10
print(soma)
