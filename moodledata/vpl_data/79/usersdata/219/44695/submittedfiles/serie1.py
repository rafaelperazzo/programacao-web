# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
soma=0
d=1
for n in range (1,n+1,1):
    if n%2==0:
        soma=soma-1/d
    else:
        soma=+1/d
        d=d+1
print(soma)

