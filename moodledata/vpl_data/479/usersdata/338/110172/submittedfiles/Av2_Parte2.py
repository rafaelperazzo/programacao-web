# -*- coding: utf-8 -*-
import math
n = int(input('digite um número: '))
m = int(input('digite um número: '))
for i in range (0,n,1):
    x = 1
    y = 1
    if n%i == 0 and m%i == 0 :
        if i>=x and i>=y :
            if x == y :
                print(x)
        
