# -*- coding: utf-8 -*-

def mediaharmonica(n,b):
    h = []
    for i in range(0,n,1):
        h.append(float(input('digite a nota%d: ' % ( i+1))))
    mh = n/(1/h)
    return mh 
    
    