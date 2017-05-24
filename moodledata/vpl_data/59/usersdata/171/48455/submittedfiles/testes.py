# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
s=0
i=0
while n>0:
    s=s+(n%10)*10**i
    n=n//10
    i=i+1
print(s)