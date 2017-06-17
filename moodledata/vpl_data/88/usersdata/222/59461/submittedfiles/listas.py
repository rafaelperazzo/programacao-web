# -*- coding: utf-8 -*-
def degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferença=abs(a[i]-a[i+1])
        b.append(diferença)
    return(b)

