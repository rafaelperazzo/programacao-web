# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
div=0
while resto!=0:
    resto=a%b
    div=div+1
    a=b
    b=resto
print(a)
print(div)
