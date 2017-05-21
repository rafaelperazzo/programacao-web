# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
for i in range(1,n+1,1):
    h=i*i
    if i%2!=0:
        imp=i/h
        soma1=soma+imp
    if i%2==0:
        par=i/h
        soma2=soma+par
s=soma1-soma2
print(s)


