# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de termos a serem calculados:'))

i=0
s=0
d=1
p=0
q=0
for i in range(1,n+1,1):
    if i%2==1:
        p=(i/d)+((i//2)/d)
        d=d+1
    elif i%2==0:
        q=(i/d)+((i//2)/d)
        d=d+1
    s=p-q
print(s)