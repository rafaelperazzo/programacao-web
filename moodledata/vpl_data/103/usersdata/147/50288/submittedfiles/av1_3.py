# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=0
resto=n%m
while resto>0:
    if n//m>0:
        cont=cont+1
    n=m
    m=resto
    resto=n%m
print(res)
print(cont)