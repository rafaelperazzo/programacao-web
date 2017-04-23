# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
soma=0
termo=1
den=n
div=1
while termo<=n:
    soma=soma+div/den
    div=div+1
    den=den-1
    termo=termo+1
print('%f.5'%soma)
    


