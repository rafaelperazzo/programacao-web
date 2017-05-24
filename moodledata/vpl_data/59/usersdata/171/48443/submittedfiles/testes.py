# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
d=n//2
s=0
i=0
while d>=0:
    s=s+(n%2)*10**i
    n=n//2
    i=i+1
print(s)