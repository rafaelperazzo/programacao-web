# -*- coding: utf-8 -*-
import numpy as np

m=int(input("Digite m: "))
n=int(input("Digite n: "))
matriz=np.empty([m,n])
trans=np.empty([n,m])

for i in range(0,m,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Digite um valor: "))


        