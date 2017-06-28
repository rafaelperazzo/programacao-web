# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o numero de linhas: "))
b=int(input("Digite o numero de colunas: "))
n=np.zeros((a,b))
for i in range(0,n.shape[0],1):
    for j in range(0,n.shape[1],1):
        n[i,j]=float(input("Digite o termo: "))
for i in range(0,shape[0],1):
    