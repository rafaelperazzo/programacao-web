# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=1
resto=0
div=n//m
res=n%m
while div>0:
    div=n//m
    m=res
    n=m
    res=n%m
    cont=cont+1
    print(m)
print(cont)