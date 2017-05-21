# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
soma=0
for i in range(1,n+1,1):
    if i%2==1:
        h=i*i
        soma=soma+i/h
    else:
        soma=soma-i/h
print(soma)

