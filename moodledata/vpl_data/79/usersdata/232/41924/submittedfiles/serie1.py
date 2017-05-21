# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
S=0
num=1
den=(num**2)
termo=(num/den)
for i in range (1,n+1,1):
    if num%2==0:
        S=S-termo
    else:
        S=S+termo
    num=num+1
    termo=termo+i
    den=(num**2)
print(S)

