# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=0
div=0
resto=0
while n>0:
    resto=n%m
    div=n//m
    cont=cont+1
    n=resto//div
print(n)
print(cont)
