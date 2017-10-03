# -*- coding: utf-8 -*-
import math
n=int(input('n: '))
a=int(input('a: '))
b=int(input('b: '))
i=1
cont=0
while cont<=n-1:
    if i%a==0 or i%b==0:
        print(i)
        cont=cont+1
    i=i+1    
