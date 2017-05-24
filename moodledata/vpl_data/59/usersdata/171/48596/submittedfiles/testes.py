# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
s=0
for i in range(1,n+1,1):
    x=int(input('digite n:'))
    if x%2==0:
        s=s+x
print(s)