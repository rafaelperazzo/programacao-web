# -*- coding: utf-8 -*-
def med(a):
    media=(sum(a)/len(a))
    return media

def desvpad(a,n):
    k=0
    for i in range(0,len(a),1):
        k=k + ((a[i]-med(a))**2)
    s=((1/(n-1))*k)
    return s

import numpy as np
m=int(input("Digite m: "))
n=int(input("Digite n: "))
mat=np.empty([m,n])

for i in range(0,m,1):
    for j in range(0,n,1):
        mat[i][j]=int(input("Digite um valor: "))
    
for i in range(0,m,1):
    print("%.2f" %(med(mat[i])))
    print("%.2f" %(desvpad(mat[i])))
