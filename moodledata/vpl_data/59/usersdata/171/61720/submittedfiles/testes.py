# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    a.append(input('digite o valor:'))
for i in range(0,n,1):
    if a[i]%2==0:
        print(a[i])

