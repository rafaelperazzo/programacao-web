# -*- coding: utf-8 -*-
import math
cont=0
x=0
n=int(input('digite n:'))
i=int(input('digite i:'))
j=int(input('digite j:'))
while cont<=n:
    if x%i==0 or x%j==0:
        print(x)
        cont=cont+1
    x=x+1
    
    
