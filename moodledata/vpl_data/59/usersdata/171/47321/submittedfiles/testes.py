# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
num=1
den=1
s=0
for i in range(1,n+1,1):
    valor=num/den
    num=num+i
    den=den+(i**2)
for termo in range(1,n+1,1):
    if termo!=0:
        s=s+valor
    else:
        s=s-valor
print(s)