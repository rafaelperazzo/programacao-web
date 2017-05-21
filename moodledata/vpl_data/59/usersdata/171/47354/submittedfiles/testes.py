# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
num=1
den=1
s=0
for termo in range(1,n+1,1):
    valor=1-(num/den)
    if termo!=0:
        s=s+valor
    else:
        s=s-valor
    den=num*num
print(s)