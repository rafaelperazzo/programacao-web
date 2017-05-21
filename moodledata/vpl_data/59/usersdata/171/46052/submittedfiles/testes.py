# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o numero:'))
reverso=0
temp=n
digitos=0
while temp>0:
    temp=temp//10
    digitos=digitos+1
while n>0:
    ultimo=n%10
    reverso=reverso+(ultimo*(10**(digitos-1)))
    n=n//10
    digitos=digitos-1
print(reverso)
