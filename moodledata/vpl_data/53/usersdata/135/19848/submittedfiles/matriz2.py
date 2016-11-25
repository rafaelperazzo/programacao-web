# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def matrizMagica(matriz):
    t=0
    dp=0
    ds=0
    for k in range(0,matriz.shape[0],1):
        dp=dp+matriz[k,k]
        ds=ds+matriz[-1-k,-1-k]
    
    for i in range(0,matriz.shape[0],1):
        l=0
        c=0
        for j in range(0,matriz.shape[1],1):
            l=l+matriz[i,j]
            c=c+matriz[j,i]
        if dp!=l or dp!=c or dp!=ds:
            t=1
            break
    if t==0:
        return True
    else:
        return False
        
n=input("Entre com a dimensao n: ")
m=np.zeros((n,n))
print
for k in range(0,m.shape[0],1):
    for l in range(0,m.shape[1],1):
        print "linha %s, coluna %s"%(k,l)
        m[k,l]=input("Entre com o elemento: ")
    print

if matrizMagica(m)==True:
    print "S"
else:
    print "N"