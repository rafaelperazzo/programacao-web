# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
r=1
resto=1
cont=0
while r>0:
    r=a%b
    a=b
    b=r
    cont=cont+1
    resto=resto+1
print(resto)
print(cont)