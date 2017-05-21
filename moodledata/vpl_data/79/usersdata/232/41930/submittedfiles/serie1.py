# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
S=0
num=1
den=(num**2)
for i in range (1,n+1,1):
    if (num%2)==0:
        S=S-(num/den)
    else:
        S=S+(num/den)
    num=num+1
    den=num**2
print(S)

