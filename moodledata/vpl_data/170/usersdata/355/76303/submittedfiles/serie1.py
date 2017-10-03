# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))

d=n*n
soma=0

for termo in range(1,n+1,1):
    if termo%2==0:
        soma=soma-(n/d)
    else:
        soma=soma+(n/d)
    n=n+1 
print(soma)



