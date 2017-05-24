# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
resto=n%m
div=0
cont=0
print(resto)
while div>0:
    div=n//m
    if div>0:
        cont=cont+1
print(cont)

