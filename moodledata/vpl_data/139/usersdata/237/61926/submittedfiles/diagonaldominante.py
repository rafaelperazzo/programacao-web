# -*- coding: utf-8 -*-
import numpy as np

def soma (h):
    p=[]
    for i in range(0,h.shape[0],1):
        o=0
        for j in range(0,h.shape[1],1):
            if i!=j:
                o=o+h[i,j]
            p.append(o)
    return (p)
    
def diagonal (a,b):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                if a[i,j]<b[i]:
                    return False
    return True


a=int(input("Digite o numero de linhas: "))
n=np.zeros((a,a))
for i in range(0,n.shape[0],1):
    for j in range(0,n.shape[1],1):
        n[i,j]=float(input("Digite o termo: "))
    
b=soma(n)

if diagonal (n,b):
    print("SIM")
else:
    print("NAO")
    