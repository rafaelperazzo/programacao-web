# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
resto=n%m
cont=1
while resto>0:
    cont=cont+1
    n=m
    m=resto
    resto=n%m
print(m)
print(cont)