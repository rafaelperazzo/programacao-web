# -*- coding: utf-8 -*-
import math
n = int(input('digite um número: '))
m = int(input('digite um número: '))
for i in range (1,n+1,1):
    x = 1
    y = 1
    if n%i == 0 and m%i == 0 :
        x = i
        y = i
        print(x)
        
