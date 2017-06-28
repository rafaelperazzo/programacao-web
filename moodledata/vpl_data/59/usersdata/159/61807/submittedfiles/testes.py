# -*- coding: utf-8 -*-
import numpy as np
def simetrico(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,(a.shape[1]//2),1):
            if a[i,j]!=a[i,((a.shape[1])-1-i)]:
                return False
    return True            

n=int(input('N de linhas:'))
a=np.zeros((n,n))    

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Valor:'))

if simetrico(a):
    print('S')
else:
    print('N')
