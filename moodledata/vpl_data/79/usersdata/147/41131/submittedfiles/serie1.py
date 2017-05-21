# -*- coding: utf-8 -*-
import math
n=int(input('digite quantidade de numeros:'))
x=1
for i in range (1,n+1,1):
    if i%2==0:
        s=(i-2)/x
    else:
        s=(i)/x
    x=(x+1)**2
print(s)

