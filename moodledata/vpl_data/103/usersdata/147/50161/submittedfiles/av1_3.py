# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=1
resto=0
div=n//m
res=n%m
while div>0:
    cont=cont+1
    div=m//res
    m=res
    print(m)
print(cont)