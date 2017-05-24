# -*- coding: utf-8 -*-
import math
n=int(input('digite n1:'))
m=int(input('digite n2:'))
cont=0
resto=n%m
while x>0:
    x=n//m
    resto=n%m
    cont=cont+1
    n=resto//x
print(n)
print(cont)
