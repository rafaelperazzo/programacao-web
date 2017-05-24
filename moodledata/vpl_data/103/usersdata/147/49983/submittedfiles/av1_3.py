# -*- coding: utf-8 -*-
import math
n=int(input('digite n1:'))
m=int(input('digite n2:'))
cont=0
resto=n%m
div=n
while n>0:
    resto=n%m
    div=n//m
    cont=cont+1
    n=resto//div
print(n)
print(cont)
