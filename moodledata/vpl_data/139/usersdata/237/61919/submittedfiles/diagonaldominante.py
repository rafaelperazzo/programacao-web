# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o numero de linhas: "))
n=np.zeros((a,a))
for i in range(0,n.shape[0],1):
    for j in range(0,n.shape[1],1):
        n[i,j]=float(input("Digite o termo: "))
for i in range(0,n.shape[0],1):
    o=0
    for j in range(0,n.shape[1],1):
        o=o+n[i,j]
    if n[i,i]<=o:
        o=o*0
    else:
        break
if o==0:
    print("SIM")
else :
    print("NAO")
    