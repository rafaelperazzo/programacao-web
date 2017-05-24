# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
x=int(input('digite x:'))
exp=1
den=1
i=0
for termo in range(1,n+1,1):
    if termo%2 !=0:
        valor=(x**exp)/exp*math.factorial(den)
        i=i+valor
    else:
        valor=(x**exp)/exp*math.factorial(den)
        i=i-valor
    exp=exp+2
    den=den+1
print(i)