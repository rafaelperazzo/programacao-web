# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
import numpy as np
def produto(a,b):
    c=np.zeros((a.shape[0],a.shape[1]))
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=0
            for r in range(0,a.shape[1],1):
                soma=soma+a[i,r]+b[r,j]
            c[i,j]=soma
    
n=int(input('digite n:'))
m=int(input('digite n:'))
a=np.zeros((n,m))
b=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite numero:'))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
 b[i,j]=float(input('digite numero de b:'))        
print(produto(a,b))
    