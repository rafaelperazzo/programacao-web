# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
num=1
S=0
if n<0:
    n=n*(-1)
for i in range (1,n+1,1):
    S=S+(num/n)
n=n-1
num=num+1
print('%.5f'%S)

