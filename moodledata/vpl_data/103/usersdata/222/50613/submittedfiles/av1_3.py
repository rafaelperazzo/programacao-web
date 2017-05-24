# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
r=1
cont=0
while r>0:
    resto=a%b
    a=b
    b=r
    cont=cont+1
print(r)
print(cont)