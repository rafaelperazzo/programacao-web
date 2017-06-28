# -*- coding: utf-8 -*-
import numpy as np
def transposta(b):
    b=[]
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            b[i,j]==a[j,i]
n=int(input('linas:'))
m=int(input('colunas:'))
b=b.zeros((n,m))
print(transposta(b))