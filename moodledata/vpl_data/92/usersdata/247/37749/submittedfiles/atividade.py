# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
if n<0:
    n=(n*-1)
soma=0
termo=1
den=n
div=1
while div<=n:
    soma=soma+div/den
    div=div+1
    den=den-1
    termo=termo+1
print('%.5f'%soma)
    


