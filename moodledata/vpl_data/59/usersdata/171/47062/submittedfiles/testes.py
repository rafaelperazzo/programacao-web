# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
m=int(input('digite m:'))
j=int(input('digite j:'))
for temp in range(1,n+1,1):
    if temp%m==j%m:
        print(temp)

