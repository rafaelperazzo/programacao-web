# -*- coding: utf-8 -*-
import math
l=[1]
x1=int(input('')) 
def fatoracao(y):
    for i in range(2,y,1):
        if x1%i==0:
            x1=x1/i
            l+=[i]
        else:
            continue
        return(l)
print(fatoracao(x1))