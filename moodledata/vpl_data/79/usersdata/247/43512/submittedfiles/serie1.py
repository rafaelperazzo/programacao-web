# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
d=0
c=0
soma=0
t=1
while t<=n:
    d=d+1
    c=d**2
    t=t+1
    if t%2==0:
        soma=soma-(d//c)
    else:
        soma=soma+(d//c)
    print(d)
    
    