# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
dividendo=a
divisor=b
cont=0
while dividendo>divisor:
    resto=dividendo%divisor
    resto=divisor%resto
    divisor=resto
    cont=cont+1
print(resto)
print(cont)
  
    