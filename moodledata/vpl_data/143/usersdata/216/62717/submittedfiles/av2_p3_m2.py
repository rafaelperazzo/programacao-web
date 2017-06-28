# -*- coding: utf-8 -*-
def diferenca(a):
    l=[]
    for i in range(0,len(a)-1,1):
        menos=a[i]-a[i+1]
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
    return(l)
    
def maior(a): return max(a)
