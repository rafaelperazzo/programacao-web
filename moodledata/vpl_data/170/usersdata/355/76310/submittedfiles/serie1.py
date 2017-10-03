# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))

m=1
d=n*n
soma=0

for termo in range(1,n+1,1):
    if termo%2==0:
        soma=soma-(m/d)
    else:
        soma=soma+(m/d)
    m=m+1
print(soma)



