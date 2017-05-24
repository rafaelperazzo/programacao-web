# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
x=int(input('digite x:'))
exp=1
den=0
i=0
for termo in range(1,n+1,1):
    valor=x-(x**exp/exp*math.factorial(den))
    if termo%2 !=0:
        i=i+valor
    else:
        i=i-valor
    exp=exp+2
    den=den+1
print(i)