# -*- coding: utf-8 -*-
import math
def fatoracao(y):
    l=[1]
    for i in range(2,y,1):
        if y%i==0:
            y=y/i
            l+=[i]
        else:
            continue
        return(l)
x1=int(input('')) 
print(fatoracao(x1))