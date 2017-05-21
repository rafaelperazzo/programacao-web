# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
soma=0
for i in range(1,n+1,1):
    h=i*i
    if i%2==1:
        soma=soma+i/h
    else:
        soma=soma-i/h
print(soma)

