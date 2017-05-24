# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=0
div=1000
resto=0
while div>0:
    div=n//m
    resto=n%m
    n=m
    m=resto
    cont=cont+1
print(div)
print(cont)
