# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
d=1
c=1
soma=0
t=1
while t<=n:
    d=d+1
    c=d**2
    a=d/c
    t=t+1
    if t%2==0:
        soma=soma-a
    else:
        soma=soma+a
print(soma)
    
    