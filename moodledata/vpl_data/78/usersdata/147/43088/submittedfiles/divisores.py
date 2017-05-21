# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
i=int(input('digite i:'))
j=int(input('digite j:'))
for x in range(0,n,1):
    if x%i==0 or x%j==0:
        print(x)
    
