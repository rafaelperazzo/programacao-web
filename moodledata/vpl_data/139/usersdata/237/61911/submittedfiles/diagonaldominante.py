# -*- coding: utf-8 -*-
import numpy as np
a=int(imput("Digite o numero de linhas: "))
b=int(imput("Digite o numero de colunas: "))
n=np.zeros((a,b))
for i in range(0,n.shape[0],1):
    for j in range(0,n.shape[1],1):
        n[i,j]=float(imput("Digite o termo: "))
print(n)